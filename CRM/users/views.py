from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from . forms import LoginForm, RegisterForm


def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            raw_password = form.cleaned_data["password1"]
            User.objects.create_user(email=email, username=username, password=raw_password)
            user = authenticate(email=email, username=username, password=raw_password)
            login(request, user)
            return redirect('/dashboard/')
    else:
        form = RegisterForm()
    context = {
        "form" : form
    }
    return render(request, "registration.html", context)


def Login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/dashboard/')
    else:
        form = LoginForm()
    context = {
        "form": form
    }
    return render(request, "login.html",context)
