from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from itsRepo.forms import CreateUserForm
from django.contrib.auth.models import Group
from itsRepo.models import Student

class RegisterPage(View):

	def get(self, request):
		form = CreateUserForm()
		if request.user.is_authenticated:
			return redirect('home_admin')
		context = {'form':form}
		return render(request, 'register.html', context)

	def post(self, request):
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')
				Student.objects.create(
					user = user,
					username = user.username,
					first_name = user.first_name,
					last_name = user.last_name,
					email = user.email
				)
				messages.success(request, 'Cuenta creada para: ' + username)

				return redirect('login')
		context = {'form':form}
		return render(request, 'register.html', context)
				

