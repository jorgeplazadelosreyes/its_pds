from django.views import View
from itsRepo.models import Student
from django.shortcuts import render

class ViewStudents(View):
    def get(self, request):
        students = Student.objects.all()
        context = {
            "students": students
        }
        return render(request, "view_students.html", context)
