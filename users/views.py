from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from users.utility import generate_code


def login_view(request):
	return render(request, "registration/login.html")


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
		code = generate_code()
		print(code)
		return render(request, template_name="registration/verification_code.html")
	else:
		return render(request, "registration/signup.html")


def verification_view(request):
	return render(request, "registration/verification_code.html")
