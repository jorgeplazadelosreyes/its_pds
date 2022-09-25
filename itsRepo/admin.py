from django.contrib import admin

from itsRepo.models import Homework, Student
# Register your models here.

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass