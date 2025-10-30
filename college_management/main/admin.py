from django.contrib import admin
from .models import Course, Subject, Teacher, Student, Attendance, Marks

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Marks)