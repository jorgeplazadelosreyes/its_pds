from itsRepo.models import Homework
from django.views import View
from django.shortcuts import render

class EditForces(View):
    def get(self, request, homework_id):
        return render(request, "edit_forces.html", homework_id)