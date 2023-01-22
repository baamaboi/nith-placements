import re

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

from .models import Student

email_pre = re.compile(
    r'^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
)


class StudentBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        student = None
        passwd_valid = False
        try:
            if email_pre.match(username):
                student = Student.objects.get(email=username)
            else:
                return None
        except Student.DoesNotExist:
            return None
        if student:
            if student.password == None:
                return None
            passwd_valid = check_password(password, student.password)
            if passwd_valid:
                return student
        return None

    def get_user(self, user_id):
        try:
            return Student.objects.get(pk=user_id)
        except Student.DoesNotExist:
            return None
