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
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            soup = str(soup.findAll('table'))
            return soup
        raise Exception(f'Response returned with Status Code: {response.status_code}')

    def clean_data(self):
        