from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate
from django.db import IntegrityError


class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"input100", "name":"username"}))
    password = forms.CharField(max_length=31, widget=forms.PasswordInput(attrs={"class":"input100", "name":"password"}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Check your username or password")

def is_same_password(password1, password2):
    return password1 == password2


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"textbox", "placeholder":"username", "name":"username"}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"class":"textbox", "placeholder": "Email", "name":"email"}))
    password1 = forms.CharField(max_length=31, widget=forms.PasswordInput(attrs={"class":"textbox", "placeholder":"Password", "name":"password1"}))
    password2 = forms.CharField(max_length=31, widget=forms.PasswordInput(attrs={"class":"textbox", "placeholder":"Confirm Password", "name":"password2"}))



    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2:
            if  not is_same_password(password1, password2):
                raise forms.ValidationError("The passwords are not identical")


    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            pass
        else:
            raise forms.ValidationError("Email already taken")
        return email
        
    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            pass
        else:
            raise forms.ValidationError("Username already taken")
        
        return username