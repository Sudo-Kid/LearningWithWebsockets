from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class Register(UserCreationForm):
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class Login(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')
