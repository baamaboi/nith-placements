from bs4 import BeautifulSoup
import re, requests
import pandas as pd

URL = 'http://14.139.56.19/scheme19/studentresult/result.asp'

class result():
    def __init__(self, roll):
        self.roll = roll
        self.raw_data = self.__get_individual_data(roll)
        self.clean_data = []

    @staticmethod
    def __get_individual_data(roll_number):
        post_data = {"RollNumber": str(roll_number), "B1": "Submit"}
        response = requests.post(URL, data=post_data, timeout=3)
        pattern = re.compile('sgpi', re.IGNORECASE)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            soup = str(soup.findAll('table'))
            if bool(re.search(pattern, soup)):
                return soup
            raise Exception('Result not found')
        raise Exception(f'Response returned with Status Code: {response.status_code}')

    def clean_data(self):
        df_list = pd.read_html(self.raw_data)
        df_list = df_list[1:-1]
        # Basic Information Extract
        base = df_list[0]
        base = [' '.join(base[i][0].split()[2:]) for i in base]
        fname = mname = lname = ''
        name_list = base[1].split()
        fname = name_list[0].strip()
        if len(name_list) > 1:
            lname = name_list[-1].strip()
            mname = ' '.join(name_list[1:-1])
        base = {'ROLL NUMBER': base[0], 'FIRST NAME': fname, 'MIDDLE NAME': mname, 'LAST NAME': lname, 'FATHER NAME': base[2]}
        
        # Semester Table Extract 
        raw_semester_tables = df_list[1::2]
        semester = []
        for df in raw_semester_tables:
            df.drop(0, axis=1, inplace=True)
            df.drop(0, inplace=True)
            df.columns = df.iloc[0]
            df.drop(index=df.index[0], axis=0, inplace=True)
            df['Sub GP'] = df['Sub GP'].astype(int)
            df['Sub Point'] = df['Sub Point'].astype(int)
            semester.append(df)
        
        # Semester Summary Extract
        summ = []
        raw_semester_summary = df_list[2::2]
        for df in raw_semester_summary:
            df.columns = ['Semester', 'SGPI', 'Semester Credits', 'CGPI', 'Total Credits']
            df['SGPI'] = df['SGPI'].apply(lambda x: x[x.index('=') + 1:])
            df['CGPI'] = df['CGPI'].apply(lambda x: x[x.index('=') + 1:])
            for key in ['Semester', 'Semester Credits', 'Total Credits']:
                df[key] = df[key].apply(lambda x: re.sub('\D', '', x))
            for key, typ in zip(df.columns, [int, float, int, float, int]):
                df[key] = df[key].astype(typ)
            summ.append(df)


        semester = pd.concat(semester, ignore_index=True)
        summ = pd.concat(summ, ignore_index=True)
        self.clean_data =  [base, semester, summ]
            