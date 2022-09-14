from django.http import HttpResponse
from itsRepo.models import Homework
from django.views import View
from itsRepo.models import Homework

class SaveFile(View):
    def post(self, request, homework_id):
        file_statement = request.POST.get("file_statement")
        homework = Homework.objects.get(id=homework_id)
        homework.statement_file = file_statement
        print(file_statement)
        homework.save()
        return HttpResponse("ok", status = 200)