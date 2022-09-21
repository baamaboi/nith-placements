from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Company,
    PlacementsAndInterns,
    Result,
    ResultSummary,
    Student,
    Subject,
    MyUser,
)

# Register your models here.


class MyUserAdmin(UserAdmin):
    fieldsets = (
        UserAdmin.fieldsets[0],
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "nith_email",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_superuser",
                    "is_staff",
                    "is_core_tpr",
                    "is_tpr",
                    "is_jtpr",
                    "is_student",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Other",
            {"fields": ("roll",)},
        ),
    )
    exclude = []


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Result)
admin.site.register(ResultSummary)
admin.site.register(Subject)
admin.site.register(PlacementsAndInterns)
admin.site.register(Student)
admin.site.register(Company)
