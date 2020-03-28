from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from . forms import LoginForm, RegisterForm, ChangePasswordForm


def registration(request):
    ''' registration view '''
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            raw_password = form.cleaned_data["password1"]
            User.objects.create_user(
                email=email, username=username, password=raw_password)
            user = authenticate(
                email=email, username=username, password=raw_password)
            login(request, user)
            return redirect('/dashboard/')
    else:
        form = RegisterForm()
    context = {
        "form": form
    }
    return render(request, "users/registration.html", context)


def Login(request):
    ''' login view '''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/dashboard/')
    else:
        if request.user.is_authenticated:
            return redirect("/dashboard/")
        else:
            form = LoginForm()
    context = {
        "form": form
    }
    return render(request, "users/login.html", context)


@login_required(login_url='/')
def change_password(request):
    ''' change password view '''
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            return redirect("/change_done/")
    else:
        form = ChangePasswordForm()
    context = {
        "form": form,
    }
    return render(request, "users/password_change.html", context)


def password_change_done(request):
    ''' password change done view '''
    return render(request, "users/password_change_done.html")
