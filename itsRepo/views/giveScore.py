from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse


from itsRepo.models import Homework

class GiveScore(View):
    def post(self, request, homework_id):
        homework = Homework.objects.get(id=homework_id)
        score = homework.difficulty
        diff = homework.final_stage - homework.initial_stage + 1
        diffs = {
            1:4,
            2:3,
            3:2,
            4:1,
        }
        mount = diffs[diff]
        plus = int(score / diffs[diff]) + (score % diffs[diff] > 0)
        request.user.student.elo_score += plus
        request.user.student.save()
        return HttpResponse("ok", status = 200)
