from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import (
    Courses,
    CustomUser,
    Staffs,
    Students,
)  # Import your CustomUser model
import logging
from django.contrib.auth.hashers import make_password


def admin_home(request):
    return render(request, "school_system/hod_template/home_content.html")


def add_staff(request):
    return render(request, "school_system/hod_template/add_staff.html")


def add_staff(request):
    return render(request, "school_system/hod_template/add_staff.html")


logger = logging.getLogger(__name__)


def add_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = request.POST.get("username")
        address = request.POST.get("address")

        try:
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=make_password(password),
                address=address,
                user_type=2,
            )
            user = Staffs.address.add(address=address)
            user.save()

            messages.success(request, "Successfully added staff")
            return HttpResponseRedirect("/add_staff")
        except:
            messages.error(request, "Failed to add staff")
            return HttpResponseRedirect("/add_staff")


def add_course(request):
    return render(request, "school_system/hod_template/add_course.html")


def add_course_save(request):
    if request.method != "POST":
        return HttpResponseRedirect("Method Not Allowed")
    else:
        course = request.POST.get("course")
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Successfully added course")
            return HttpResponseRedirect("/add_course")
        except Exception as e:
            messages.error(request, f"Failed to add course: {e}")
            return HttpResponseRedirect("/add_course")


def add_student(request):
    courses = Courses.objects.all()
    return render(
        request, "school_system/hod_template/add_student.html", {"courses": courses}
    )


def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = request.POST.get("username")
        address = request.POST.get("address")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        course_id = request.POST.get("course")
        sex = request.POST.get("sex")
        try:
            user = CustomUser.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=make_password(password),
                address=address,
                user_type=3,
            )
            user = Students.address = address
            course_objs = Courses.objects.get(id=course_id)
            user.students.course_id = course_objs
            user.Students = session_start = session_start
            user.student = session_end = session_end
            user.student.gender = sex
            user.students.profile_pic = ""
            user.save()

            messages.success(request, "Successfully added student")
            return HttpResponseRedirect("/add_student")
        except:
            messages.error(request, "Failed to add student")
            return HttpResponseRedirect("/add_student")
