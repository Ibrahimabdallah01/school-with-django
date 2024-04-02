from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver

# Create your models here.


# user role
class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staffs"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    address = models.TextField(default="")


# admin
class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # email = models.CharField(max_length=255)
    # password = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# staffs
class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # name = models.CharField(max_length=255)
    # email = models.CharField(max_length=255)
    # password = models.CharField(max_length=255)
    address = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_At = models.DateTimeField(auto_now=True)
    objects = models.Manager()


# classes
class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


# subject
class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    Course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    staffs_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# students
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # name = models.CharField(max_length=255)
    # email = models.CharField(max_length=255)
    # password = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    profile_pc = models.FileField()
    address = models.TextField()
    Course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# attendance
class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    Subjects_id = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING)
    Attendance_date = models.DateTimeField(auto_now_add=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# attendance Record
class AttendanceRecord(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    Attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    students = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# leave Report
class leaveReportStudent(models.Model):
    id = models.AutoField(primary_key=True)
    students_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# leave staffs
class leaveReportStaffs(models.Model):
    id = models.AutoField(primary_key=True)
    staffs_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# feedback students
class FeedbackStudent(models.Model):
    id = models.AutoField(primary_key=True)
    students_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# feedback staffs
class FeedBackStaffs(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# notification student


class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    students_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class NotificationStaffs(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


# will run only when data added on CustomUser
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.user_type == 1:
        AdminHOD.objects.create(admin=instance)
    if instance.user_type == 2:
        Staffs.objects.create(admin=instance)
    if instance.user_type == 3:
        Students.objects.create(admin=instance)


# this method will call after create user method execution
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.staffs.save()
    if instance.user_type == 3:
        instance.Students.save()
