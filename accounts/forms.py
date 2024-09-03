from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()


class ChangePassword(forms.Form):
    current_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=20, widget=forms.PasswordInput)

class PasswordResetForm(forms.Form):
    email = forms.EmailField()

class PasswordResetConfirmForm(forms.Form):
    pass1 = forms.CharField(max_length=20, widget=forms.PasswordInput)
    pass2 = forms.CharField(max_length=20, widget=forms.PasswordInput)