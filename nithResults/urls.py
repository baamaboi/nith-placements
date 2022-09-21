from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),
    path("accounts/", include("allauth.urls")),
    path("debug/", include("debug_toolbar.urls"), name="debug_toolbar"),
]
