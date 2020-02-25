from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"class":"input100"}))
    password = forms.CharField(max_length=31, widget=forms.PasswordInput(attrs={"class":"input100"}))

def is_same_password(password1, password2):
    return password1 == password2


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"class":"textbox", "placeholder": "Email", "name":"email"}))
    password1 = forms.CharField(max_length=31, widget=forms.PasswordInput(attrs={"class":"textbox", "placeholder":"Password", "name":"password1"}))
    password2 = forms.CharField(max_length=31, widget=forms.PasswordInput(attrs={"class":"textbox", "placeholder":"Confirm Password", "name":"password2"}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
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
            raise forms.ValidationError("Email already taken")
        except:
            pass