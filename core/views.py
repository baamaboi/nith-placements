from rest_framework import generics
from rest_framework.permissions import (
    SAFE_METHODS,
    AllowAny,
    BasePermission,
    IsAdminUser,
)

from core.models import Company, ResultSummary, Student
from core.serializers import *

# Permissions


class StudentDetailPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user.roll


# Create your views here.


class StudentList(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [StudentDetailPermission, IsAdminUser]
    queryset = Student.objects.all()
    serializer_class = StudentDetailsSerializer


class CompanyDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Company.objects.all()
    serializer_class = CompanyDetailsPublicSerializer

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return CompanyDetailsSerializer
        return CompanyDetailsPublicSerializer


class CompanyList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer


class ResultList(generics.ListAPIView):
    queryset = ResultSummary.objects.all()
    serializer_class = ResultPublicSerializer
