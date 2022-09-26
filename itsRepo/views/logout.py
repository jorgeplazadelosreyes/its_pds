from django.views import View
from django.shortcuts import redirect 
from django.contrib.auth import logout

class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('login')