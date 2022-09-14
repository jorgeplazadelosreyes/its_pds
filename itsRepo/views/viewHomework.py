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
        initial_stage = request.POST.get("initial_stage")
        final_stage = request.POST.get("final_stage")
        dificultad = request.POST.get("difficulty")

        homework = Homework.objects.get(id=homework_id)

        homework.statement_text = str(s_statement)
        homework.diagram = str(dcl)
        homework.difficulty = int(dificultad)
        homework.Fx = str(Fx)
        homework.Fy = str(Fy)
        homework.Fm = str(Fm)
        homework.initial_stage = int(initial_stage)
        homework.final_stage = int(final_stage)
        
        homework.save()
        return HttpResponse("ok", status = 200)