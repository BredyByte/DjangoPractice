from django.contrib import auth
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm

def login(request):
	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username, password=password)
			if user:
				auth.login(request, user)
				return HttpResponseRedirect(reverse('main:index'))
	else:
		form = UserLoginForm()


	context = {
		'title': 'Home - Authorization',
		'form': form
	}

	return render(request, 'users/login.html', context)

def registration(request):

	if request.method == 'POST':
		form = UserRegistrationForm(data=request.POST)
		if form.is_valid():
			form.save()
			"""
			Для того чтобы автологинить юзера, если не хочешь автологинить,
			убери эту линию и редиректи на авторизационную страницу
			"""
			user = form.instance
			auth.login(request, user)
			return HttpResponseRedirect(reverse('main:index'))
	else:
		form = UserRegistrationForm()

	context = {
		'title': 'Home - Registration',
		'form': form
	}

	return render(request, 'users/registration.html', context)

def profile(request):
	if request.method == 'POST':
		form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect(reverse('user:profile'))
	else:
		form = ProfileForm(instance=request.user)

	context = {
		'title': 'Home - Profile',
		'form': form
	}

	return render(request, 'users/profile.html', context)

def logout(request):
	auth.logout(request)
	return redirect(reverse('main:index'))
