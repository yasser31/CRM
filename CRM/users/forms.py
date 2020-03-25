from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate
from django.db import IntegrityError


class LoginForm(forms.Form):
    ''' user login form '''
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "input100", "name": "username",
               "placeholder": "Username"}))
    password = forms.CharField(max_length=31, widget=forms.PasswordInput(
        attrs={"class": "input100", "name": "password",
               "placeholder": "Password"}))

    def clean(self):
        ''' form validation '''
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Check your username or password")


def is_same_password(password1, password2):
    ''' validate that the password are the same '''
    return password1 == password2


class RegisterForm(forms.Form):
    ''' registration form  '''
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "username",
               "name": "username"}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "Email", "name": "email"}))
    password1 = forms.CharField(max_length=31, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Password",
               "name": "password1"}))
    password2 = forms.CharField(max_length=31, widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Confirm Password",
               "name": "password2"}))

    def clean(self):
        ''' password validation '''
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2:
            if not is_same_password(password1, password2):
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
        ''' validate email does not exists'''
        username = self.cleaned_data.get("username")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            pass
        else:
            raise forms.ValidationError("Username already taken")

        return username

    def clean_password1(self):
        ''' validate passwords '''
        count_digit = 0
        count_sp_char = 0
        count_up = 0
        count_low = 0
        count_alpha = 0
        errors = []
        password1 = self.cleaned_data["password1"]
        if len(password1) < 8:
            raise forms.ValidationError(
                "Password should contain at least 8 characters")
        for st in password1:
            if st.isdigit():
                count_digit += 1
            elif not st.isdigit() and not st.isalpha():
                count_sp_char += 1
            elif st.islower():
                count_low += 1
            elif st.isupper():
                count_up += 1

        if count_digit == 0:
            errors.append("Password must contain a digit")
        if count_up == 0:
            errors.append(
                "Password must contain an upper case")
        if count_sp_char == 0:
            errors.append("Password must contain a special character")
        if count_low == 0:
            errors.append("Password must contain a lower case")
        if len(errors) > 0:
            raise forms.ValidationError(errors)
        return password1


class ChangePasswordForm(forms.Form):
    ''' change password form '''
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"placeholder": "Username", "name": "username",
               "class": "text"}))
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={"placeholder": "Old Password", "name": "old_password",
               "class": "text"}))
    new_password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={"placeholder": "New Password", "name": "new_password",
               "class": "text"}))
    confirm_password = forms.CharField(max_length=100,
                                       widget=forms.PasswordInput(
                                           attrs={"placeholder": "Confirm Password",
                                                  "name": "confirm_password",
                                                  "class": "text"}))

    def clean(self):
        ''' form validation '''
        cleaned_data = super().clean()
        password1 = cleaned_data["new_password"]
        password2 = cleaned_data["confirm_password"]
        count_digit = 0
        count_sp_char = 0
        count_up = 0
        count_low = 0
        count_alpha = 0
        errors = []
        if len(password1) < 8:
            raise forms.ValidationError(
                "Password should contain at least 8 characters")
        for st in password1:
            if st.isdigit():
                count_digit += 1
            elif not st.isdigit() and not st.isalpha():
                count_sp_char += 1
            elif st.islower():
                count_low += 1
            elif st.isupper():
                count_up += 1
        if count_digit == 0:
            errors.append("Password must contain a digit")
        if count_up == 0:
            errors.append(
                "Password must contain an upper case")
        if count_sp_char == 0:
            errors.append("Password must contain a special character")
        if count_low == 0:
            errors.append("Password must contain a lower case")
        if len(errors) > 0:
            raise forms.ValidationError(errors)
        if not is_same_password(password1, password2):
            raise forms.ValidationError("The passwords are not identical")

        return password1

    def clean_old_password(self):
        ''' old password and username validation '''
        old_password = self.cleaned_data["old_password"]
        username = self.cleaned_data["username"]
        user = authenticate(username=username, password=old_password)
        if user is None:
            raise forms.ValidationError("Password or Username is not correct")
        return old_password
