from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login

class LoginPage(View):

	def get(self, request):
		if request.user.is_authenticated:
			return redirect('home_admin')
		else:
			context = {}
			return render(request, 'login.html', context)

	def post(self, request):
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home_admin')
			else:
				messages.info(request, 'Username OR password is incorrect')
		context = {}
		return render(request, 'login.html', context)
