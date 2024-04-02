import datetime
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from school_system.EmailBackEnd import EmailBackEnd
from django.contrib import messages


# Create your views here.
def base(request):
    # return HttpResponse("Hello king")
    return render(request, "school_system/base.html")


# def add_staff(request):
#     return render(request, "school_system/hod_template/add_staff.html")


def LoginPage(request):
    return render(request, "school_system/my_login.html")


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        user = EmailBackEnd.authenticate(
            request,
            username=request.POST.get("email"),
            password=request.POST.get("password"),
        )
        if user != None:
            login(request, user)
            return HttpResponseRedirect("admin_home")
        else:
            messages.error(request, "invald login details")
            return HttpResponseRedirect("/")


def GetUserDetails(request):
    if request.user != None:
        return HttpResponse(
            "User : " + request.email.user + "usertype : " + request.user.user_type
        )
    else:
        return HttpResponse("Please login first")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
