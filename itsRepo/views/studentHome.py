from django.views import View
from django.shortcuts import render
from itsRepo.models import Homework

class StudentHome(View):
    def get(self, request):   
        score = request.user.student.elo_score
        next_homework = Homework.objects.filter()
        context = {
            "score": score
        }
        return render(request, 'student_home.html', context)