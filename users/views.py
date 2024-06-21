from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from users.decorators import redirect_authenticated_user
from carts.models import Cart

@redirect_authenticated_user
def login(request):
	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username, password=password)

			"""
			Добавляем юзеру его сессионный ключ, который он получил будучи не авторизованным,
			чтобы иметь доступ к своей карзине, так как если мы еготого не сделаем,
			джанго полсе авторизации ему даст дургой, и мы потерем его корзиину,
			которая как форейн ки имееет сессию юзера
			"""
			session_key = request.session.session_key

			if user:
				auth.login(request, user)
				"""
				Может быть много месседжей в контроллере в одночасье: worning, error и тдю
				Поэтому в html разметке includes/notifications.html можно заметить цикл massage in messages
				И так же. Это контекстная переменная, которая сама переедается в тимплейт, поэтому ее нет в контексте контроллера
				"""
				messages.success(request, f"{username}, you have successfully logged in!")

				"""
				Будучи ананимом, при регистрации или логине,
				будет добавляться все продукты с анонима в
				зарегестриррованного / залогиненного юзера
				"""
				if session_key:
					Cart.objects.filter(session_key=session_key).update(user=user)
				redirect_page = request.POST.get('next', None)
				if redirect_page and redirect_page != reverse('user:logout'):
					return redirect(request.GET.get('next'))

				return redirect(reverse('user:profile'))
	else:
		form = UserLoginForm()


	context = {
		'title': 'Home - Authorization',
		'form': form
	}

	return render(request, 'users/login.html', context)

@redirect_authenticated_user
def registration(request):
	if request.method == 'POST':
		form = UserRegistrationForm(data=request.POST)
		if form.is_valid():
			form.save()

			session_key = request.session.session_key

			"""
			Для того чтобы автологинить юзера
			"""
			user = form.instance
			auth.login(request, user)

			"""
			Будучи ананимом, при регистрации или логине,
			будет добавляться все продукты с анонима в
			зарегестриррованного / залогиненного юзера
			"""
			if session_key:
				Cart.objects.filter(session_key=session_key).update(user=user)

			messages.success(request, f"{user.username}, you have successfully registered!")
			return redirect(reverse('main:index'))
	else:
		form = UserRegistrationForm()

	context = {
		'title': 'Home - Registration',
		'form': form
	}

	return render(request, 'users/registration.html', context)

@login_required
def profile(request):
	if request.method == 'POST':
		form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, "Your changes have been successfully applied!")
			return redirect(reverse('user:profile'))
	else:
		form = ProfileForm(instance=request.user)

	context = {
		'title': 'Home - Profile',
		'form': form
	}

	return render(request, 'users/profile.html', context)

def users_cart(request):
	return render(request, 'users/users-cart.html')

@login_required
def logout(request):
	messages.success(request, "You have successfully logged out!")
	auth.logout(request)
	return redirect(reverse('user:login'))
