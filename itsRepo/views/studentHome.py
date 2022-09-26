from django.views import View
from django.shortcuts import render
from itsRepo.models import Homework

class StudentHome(View):
    def get(self, request):   
        score = request.user.student.elo_score
        homeworks = Homework.objects.all()
        ids = []
        sus = [] 

        for homework in homeworks:
            ids.append(homework.id)
            sus.append(homework.difficulty - score)

        count = 0
        num = 9999999
        select = 0
        for sm in sus:
            if sm < num:
                num = sm
                select = count
            count += 1       
        id_selected = ids[select]

        next_homework = Homework.objects.get(id = id_selected)

        stage = 'diagram_forces'
        if next_homework.initial_stage == 2:
            stage = 'edit_forces'
        if next_homework.initial_stage == 4:
            stage = 'balance_equations'
        
        print(stage)
        context = {
            "score": score,
            "next_homework": next_homework,
            "stage": stage
        }
        return render(request, 'student_home.html', context)