from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("student/", views.StudentList.as_view()),
    path("student/<int:pk>/", views.StudentDetail.as_view()),
    path("company/", views.CompanyList.as_view()),
    path("company/<int:pk>/", views.CompanyDetail.as_view()),
    path("result/", views.ResultList.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
