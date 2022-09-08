from django.contrib import admin

from itsRepo.models import Homework, Student, User
# Register your models here.

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
