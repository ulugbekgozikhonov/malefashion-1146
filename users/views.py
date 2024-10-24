from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def signup_view(request):
	if request.method == "POST":
		username = request.POST.get("username")
		email = request.POST.get("email")
		password = request.POST.get("password")
		password_confirm = request.POST.get("password_confirm")

		if User.objects.filter(username=username).exists():
			messages.error(request, message="This username already taken")
			return redirect(request.path_info)
		if User.objects.filter(email=email).exists():
			messages.error(request, message="Email already exists")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
		if password_confirm != password:
			messages.error(request, message="Passwords not match")
			return redirect(request.path_info)

		User.objects.create_user(
			username=username,
			password=password,
			email=email
		)
		return redirect('users:login')
	else:
		return render(request, "registration/signup.html")


def login_view(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("pages:home")
		else:
			messages.error(request, "username or password error")
			return redirect(request.path_info)

	return render(request, "registration/login.html")


def logout_view(request):
	logout(request)
	return redirect('pages:home')
