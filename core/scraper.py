import asyncio
import logging
import re
from decimal import Decimal
from typing import NoReturn, Optional, Tuple, Union

import aiohttp
import environ
from bs4 import BeautifulSoup
from django.db.models import QuerySet

from .helpers import MASTER_URL, columns_sem, columns_sum, grade_map, intt
from .models import Result, ResultSummary, Student

env = environ.Env()
HOST = env("SCRAPER_HOST")

logging.basicConfig(
    level=logging.WARNING,
    filename="results.log",
    format="%(asctime)s:%(levelname)s - %(message)s",
)

pattern = re.compile("sgpi", re.IGNORECASE)
num = re.compile(r"\d+")
deci_re = re.compile(r"=(\d+(\.\d+)?)")
DUAL_DEGREE = "B. Tech. + M. Tech. (Dual Degree)"
BTECH = "B. Tech."


def clean_sem(soup: BeautifulSoup, student: Student) -> Tuple[list, int]:
    rows = soup.findAll("tr")
    return_list = []
    sem_no = num.search(rows[0].text).group(0)
    backlog_count = 0
    for row in rows[2:]:
        res = {}
        for index, data in enumerate(filter(lambda x: x, row.text.split("\n"))):
            res[columns_sem[index]] = data.strip()
        res["semester"] = int(sem_no)
        res["grade"] = intt(res["grade"])
        res["credits"] = intt(res["credits"])
        if grade_map[res["grade_letter"]] != res["grade"] // res["credits"]:
            res["grade"] = grade_map[res["grade_letter"]] // res["credits"]
        res.pop("grade_letter")
        res["roll"] = student
        return_list.append(res)
        if res["grade"] > 0 and res["grade"] < 4:
            backlog_count += 1
    return return_list, backlog_count


def clean_sum(soup: BeautifulSoup, student: Student) -> list:
    rows = soup.findAll("tr")
    as_type = [int, Decimal, int, Decimal, int]
    return_list = []
    for row in rows:
        res = {}
        for index, data in enumerate(filter(lambda x: num.search(x), row.text.split("\n"))):
            data = data.strip()
            match = num.search(data).group(0)
            temp = deci_re.search(data)
            if temp:
                match = temp.group(1)
            res[columns_sum[index]] = as_type[index](match)
            res["roll"] = student
        return_list.append(res)
    return return_list


async def fetch_result(
    student: Student,
    session: aiohttp.ClientSession,
    URL: str,
    update_last: Optional[int] = None,
) -> Tuple[Student, Tuple[list, list, dict]]:
    roll_number = getattr(student, "roll", None)
    post_data = {"RollNumber": str(roll_number), "B1": "Submit"}
    result_found = True
    async with session.post(URL, data=post_data) as response:
        if response.status == 200:
            soup = BeautifulSoup(await response.read(), "lxml")
            if not bool(re.search(pattern, soup.text)):
                result_found = False
            if result_found:
                # init
                sem_result_list = []
                sem_sum_list = []
                base = {"active_backlog": getattr(student, "active_backlog", 0)}
                # making soup tasty
                soup = soup.findAll("table")[1:-1]
                soup_sum = soup[2::2]
                soup_sem = soup[1::2]
                # to create or to update ?
                if update_last:
                    soup_sum = soup[-update_last * 2 + 1 :: 2]
                    soup_sem = soup[-update_last * 2 : -1 : 2]
                # main
                for table in soup_sem:
                    sem_result, back = clean_sem(table, student)
                    sem_result_list.extend(sem_result)
                    base["active_backlog"] += back
                for table in soup_sum:
                    sem_sum_list.extend(clean_sum(table, student))
                return (student, (sem_result_list, sem_sum_list, base))
            logging.error(f"{roll_number} - Result not found")
        logging.error(f"{roll_number} - Response returned with Status Code: {response.status}")


async def fetch_many(queryset: Union[QuerySet, list[Student]], update_last: Optional[int] = None) -> list:
    async with aiohttp.ClientSession() as session:
        collect = []
        for student in queryset:
            degree = getattr(student, "degree", BTECH)
            batch = getattr(student, "roll", "00")[0:2] + "/"
            URL = HOST + getattr(MASTER_URL, degree, "scheme") + batch + "studentresult/result.asp"
            collect.append(fetch_result(student, session, URL, update_last=update_last))
            if degree == DUAL_DEGREE:
                URL = HOST + getattr(MASTER_URL, BTECH, "scheme") + batch + "studentresult/result.asp"
                collect.append(fetch_result(student, session, URL, update_last=update_last))
        res = await asyncio.gather(
            *collect,
            return_exceptions=True,
        )
    return res


def create_result(
    result: Tuple, student: Student, save: Optional[bool] = False, batch: Optional[bool] = True
) -> Tuple[Student, list[Result], list[ResultSummary]]:
    if not batch:
        res = asyncio.run(fetch_many([getattr(student, "roll", None)]))
        result = [i[1] for i in res]
    backs = getattr(student, "active_backlog", 0)
    for sem, sum, base in result:
        sem_db_list = [Result(**i) for i in sem]
        sum_db_list = [ResultSummary(**i) for i in sum]
        backs += getattr(base, "active_backlog", 0)
        for key, value in base.items():
            setattr(student, key, value)
    setattr(student, "active_backlog", backs)
    if save:
        student.save()
        Result.objects.bulk_create(sem_db_list)
        ResultSummary.objects.bulk_create(sum_db_list)
    return student, sem_db_list, sum_db_list


def create_batch_result(student_queryset: Union[QuerySet, list[Student]]) -> NoReturn:
    data = asyncio.run(fetch_many(student_queryset))
    st_all = []
    sem_all = []
    sum_all = []
    for student, data in data:
        try:
            student, sem_list, sum_list = create_result(data, student)
        except Exception as e:
            logging.error(f"{student.roll} - {student.name} : {e}")
        st_all = [*st_all, student]
        sem_all = [*sem_all, *sem_list]
        sum_all = [*sum_all, *sum_list]

    Student.objects.bulk_update(
        st_all,
        ["active_backlog", "cgpi_bachelor", "cgpi_master", "father_name"],
        batch_size=len(st_all),
    )
    Result.objects.bulk_create(sem_all)
    ResultSummary.objects.bulk_create(sum_all)
