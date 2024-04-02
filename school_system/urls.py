from django.conf import settings
from django.contrib import admin
from django.urls import path
from school_system import views
from school_system import HodViews

# from django.conf.urls.static import static

urlpatterns = [
    path("", views.LoginPage, name=""),
    path("get_user_details", views.GetUserDetails),
    path("logout_user", views.logout_user),
    path("doLogin", views.doLogin, name="doLogin"),
    path("admin_home", HodViews.admin_home),
    path("add_staff", HodViews.add_staff),
    path("add_staff_save", HodViews.add_staff_save),
    path("add_course", HodViews.add_course, name="add_course"),
    path("add_course_save", HodViews.add_course_save, name="add_course_save"),
    path("add_student", HodViews.add_student, name="add_student"),
    path("add_student_save", HodViews.add_student_save, name="add_student_save"),
]
