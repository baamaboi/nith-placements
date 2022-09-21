from rest_framework.response import Response
from django.http import Http404
from core.serializers import StudentDetailsSerializer, StudentSerializer
from core.models import Student
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


# Create your views here.


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailsSerializer
