from django.views import View
from django.shortcuts import render

class NextHomework(View):
    def get(self, request):    
        score = request.user
        context = {
            "score": score
        }
        return render(request, 'student_home.html', context)