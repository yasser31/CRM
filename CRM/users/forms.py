from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"class":"input100"}))
    password = forms.CharField(max_length=31, widget=forms.PasswordInput(attrs={"class":"input100"}))


class RegisterForm(UserCreationForm):
    
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"class":"textbox", "placeholder": "Email"}), help_text='Please provide a valid email address.')
    password1 = forms.CharField(max_length=31, widget=forms.PasswordInput(attrs={"class":"textbox", "placeholder":"Password"}))
    password2 = forms.CharField(max_length=31, widget=forms.PasswordInput(attrs={"class":"textbox", "placeholder":"Confirm Password"}))

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]