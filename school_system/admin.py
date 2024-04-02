from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from school_system.models import CustomUser

# Register your models here.

# create blank for to encrypt password


class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)
