from django.views import View
from django.shortcuts import render, redirect

class UserHome(View):
    def get(self, request):    
        context = {}
        return render(request, 'user_home.html', context)