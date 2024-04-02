from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from school import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("school_system.urls")),
]
