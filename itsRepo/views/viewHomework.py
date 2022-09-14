from django.http import HttpResponse
from itsRepo.models import Homework
from django.views import View
from itsRepo.models import Homework
from django.shortcuts import render, redirect


class ViewHomework(View):
    def post(self, request, homework_id):
        dcl = request.POST.get("diagram")
        s_statement = request.POST.get("str_statement")
        dificultad = request.POST.get("difficulty")
        Fx = request.POST.get("Fx")
        Fy = request.POST.get("Fy")
        Fm = request.POST.get("Fm")
        homework = Homework.objects.get(id=homework_id)
        homework.diagram = str(dcl)
        homework.statement_text = str(s_statement)
        homework.difficulty = int(dificultad)
        homework.Fx = str(Fx)
        homework.Fy = str(Fy)
        homework.Fm = str(Fm)
        
        homework.save()
        return HttpResponse("ok", status = 200)
