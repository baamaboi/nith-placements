from dataclasses import fields
from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["roll", "dept", "fname"]


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "roll",
            "fname",
            "mname",
            "lname",
            "father_name",
            "sex",
            "email",
            "phone_number",
            "student_email",
            "cgpi_bachelor",
            "cgpi_master",
            "dob",
            "active_backlog",
            "total_backlog",
            "twelveth_year",
            "twelveth_board",
            "twelveth_school",
            "twelveth_percent",
            "tenth_year",
            "tenth_percent",
            "tenth_board",
            "tenth_school",
            "domicile_state",
            "domicile_district",
            "domicile_place",
            "cv",
            "grad_year",
            "curr_batch",
            "pwd",
            "cluster",
            "dept",
            "degree",
        ]
