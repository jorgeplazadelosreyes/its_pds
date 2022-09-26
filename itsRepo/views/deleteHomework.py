from django.shortcuts import render, redirect
from django.views import View

from itsRepo.models import Homework

class DeleteHomework(View):
    def post(self, request, homework_id):
        homework = Homework.objects.get(id=homework_id)
        if request.method == "POST":
            homework.delete()
            return redirect("home_admin")
