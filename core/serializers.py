from rest_framework import serializers

from .models import Company, ResultSummary, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["roll", "dept", "fname"]


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class CompanyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class CompanyDetailsPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = [
            "jnf_url",
            "allowed_branches",
            "drive_start_date",
            "drive_end_date",
            "drive_engagement_date",
            "hr_details",
            "remarks",
            "spoc",
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
        fields = "__all__"
