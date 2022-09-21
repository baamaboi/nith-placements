import re, requests
from collections import Counter
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


class result:
    def __init__(self, roll, batch):
        self.roll = roll
        self.raw_data = self.__get_individual_data(roll, str(batch).strip())
        self.clean_data = self.__clean_individual_data()
        self.batch = str(batch).strip()

    @staticmethod
    def __get_individual_data(roll_number, batch):
        URL = f"http://14.139.56.19/scheme{batch[-2:]}/studentresult/result.asp"
        post_data = {"RollNumber": str(roll_number), "B1": "Submit"}
        response = requests.post(URL, data=post_data, timeout=3)
        pattern = re.compile("sgpi", re.IGNORECASE)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            soup = str(soup.findAll("table"))
            if bool(re.search(pattern, soup)):
                return soup
            raise Exception("Result not found")
        raise Exception(f"Response returned with Status Code: {response.status_code}")

    def __clean_individual_data(self):
        branch = {
            "EE": "Electrical Engineering",
            "EC": "Electronics and Communication Engineering",
            "CE": "Civil Engineering",
            "MS": "Material Science and Engineering",
            "CS": "Computer Science and Engineering",
            "CH": "Chemical Engineering",
            "ME": "Mechanical Engineering",
            "AR": "Architecture",
        }
        df_list = pd.read_html(self.raw_data)
        df_list = df_list[1:-1]
        # Basic Information Extract
        base = df_list[0]
        base = [" ".join(base[i][0].split()[2:]) for i in base]
        fname, mname, lname = "", "", ""
        name_list = base[1].split()
        fname = name_list[0].strip()
        if len(name_list) > 1:
            lname = name_list[-1].strip()
            mname = " ".join(name_list[1:-1])
        base = {
            "ROLL NUMBER": base[0],
            "FIRST NAME": fname,
            "MIDDLE NAME": mname,
            "LAST NAME": lname,
            "FATHER NAME": base[2],
            "BRANCH": "",
            "ACTIVE BACKLOGS": 0,
        }

        # Semester Table Extract
        raw_semester_tables = df_list[1::2]
        semester = []
        for df in raw_semester_tables:
            sem_no = int(df[0][0][-2:])
            df.drop(0, axis=1, inplace=True)
            df.drop(0, inplace=True)
            df.columns = df.iloc[0]
            df.drop(index=df.index[0], axis=0, inplace=True)
            df.loc[:, "Sub GP"] = df["Sub GP"].astype(int)
            df.loc[:, "Sub Point"] = df["Sub Point"].astype(int)
            df["Semester"] = [sem_no] * len(df)
            semester.append(df)

        # Semester Summary Extract
        summ = []
        raw_semester_summary = df_list[2::2]
        for df in raw_semester_summary:
            df.columns = [
                "Semester",
                "SGPI",
                "Semester Credits",
                "CGPI",
                "Total Credits",
            ]
            df.loc[:, "SGPI"] = df["SGPI"].apply(lambda x: x[x.index("=") + 1 :])
            df.loc[:, "CGPI"] = df["CGPI"].apply(lambda x: x[x.index("=") + 1 :])
            for key in ["Semester", "Semester Credits", "Total Credits"]:
                df[key] = df[key].apply(lambda x: re.sub("\D", "", x))
            for key, typ in zip(df.columns, [int, float, int, float, int]):
                df[key] = df[key].astype(typ)
            summ.append(df)

        semester = pd.concat(semester, ignore_index=True)
        semester.insert(0, "ROLL NUMBER", [self.roll] * len(semester))
        summ = pd.concat(summ, ignore_index=True)
        summ.insert(0, "ROLL NUMBER", [self.roll] * len(summ))
        base["BRANCH CODE"] = Counter(
            map(lambda x: x[0:2], list(semester["Subject Code"]))
        ).most_common(1)[0][0]
        base["BRANCH"] = branch[base["BRANCH CODE"]]
        base["CGPI"] = summ["CGPI"][len(summ) - 1]
        for grade in semester["Grade"]:
            if str(grade) == "F":
                base["ACTIVE BACKLOGS"] += 1
        return [base, semester, summ]


def batch_result(batch_list, save=False):
    data = []
    err = []
    for roll, batch in batch_list:
        try:
            r = result(roll, batch)
            data.append(r.clean_data)
        except Exception as e:
            err.append(f"Roll {roll}, Batch {batch}: {e}")

    if data == []:
        err_str = ""
        for i in err:
            err_str += i + "\n"
        raise Exception(f"Data array was empty\n{err_str}")
    data = np.array(data)
    df_base = pd.DataFrame(list(data[:, 0]))
    df_res = pd.concat(data[:, 1], ignore_index=True)
    df_summ = pd.concat(data[:, 2], ignore_index=True)

    if save == True:
        df_base.to_pickle("base.pkl")
        df_res.to_pickle("result.pkl")
        df_summ.to_pickle("result_summary.pkl")

    return [[df_base, df_res, df_summ], err]
