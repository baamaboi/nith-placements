from dataclasses import fields
from rest_framework import serializers
from .models import Student, Company, ResultSummary


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
            "phone_number1",
            "phone_number2",
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
            "tenth_board",
            "tenth_school",
            "tenth_percent",
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


class CompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "ctc_offered",
            "stipend_offered",
            "total_candidates_place",
            "jnf_url",
            "on_campus",
            "fte",
            "intern",
            "allowed_branches",
            "fte_profile",
            "intern_profile",
            "drive_start_date",
            "drive_end_date",
            "drive_engagement_date",
            "hr_details",
            "drive_status",
            "drive_result",
            "graduating_batch",
            "remarks",
            "spoc",
        ]


class CompanyDetailsPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "ctc_offered",
            "stipend_offered",
            "total_candidates_place",
            "on_campus",
            "fte",
            "intern",
            "fte_profile",
            "intern_profile",
            "drive_status",
            "drive_result",
            "graduating_batch",
        ]


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "ctc_offered",
        ]


class ResultPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultSummary
        fields = [
            "id",
            "roll",
            "semester",
            "cgpi",
            "sgpi",
            "sem_credits",
            "total_credits",
        ]
