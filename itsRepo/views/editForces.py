from itsRepo.models import Homework
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

class EditForces(View):
    def get(self, request, homework_id):
        homework = Homework.objects.get(id=homework_id)
        context = {
            "homework": homework
        }
        return render(request, "edit_forces.html", context)
    
    def post(self, request, homework_id):
        dcl = request.POST.get("diagram2")
        

        homework = Homework.objects.get(id=homework_id)
        homework.diagram2 = str(dcl)
        
        
        homework.save()
        return HttpResponse("ok", status = 200)