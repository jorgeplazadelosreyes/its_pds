from itsRepo.models import Homework
from django.views import View
from django.shortcuts import render

class EditDiagram(View):
    def get(self, request, homework_id):
        homework = Homework.objects.get(id=homework_id)
        context = {
            "homework": homework
        }
        return render(request, "edit_diagram.html", context)