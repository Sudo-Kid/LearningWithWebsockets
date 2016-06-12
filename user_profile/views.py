from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginRegister(View):
    template_name = 'user_profile/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('chat:index')

        login_form = AuthenticationForm()
        register_form = UserCreationForm()
        return render(request, self.template_name,
                      {'login_form': login_form, 'register_form': register_form})

class Login(View):
    template_name = 'user_profile/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('chat:index')

        login_form = AuthenticationForm()
        return render(request, self.template_name,
                      {'login_form': login_form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('chat:index')

        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])

            if user.is_active:
                login(request, user)
                return redirect('chat:index')

        return render(request, self.template_name,
                      {'login_form': login_form})


class Register(View):
    template_name = 'user_profile/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('chat:index')

        register_form = UserCreationForm()
        return render(request, self.template_name,
                      {'register_form': register_form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('chat:index')

        register_form = UserCreationForm(data=request.POST)

        if register_form.is_valid():
            new_user = register_form
            register_form.save()
            user = authenticate(username=new_user.cleaned_data['username'],
                                password=new_user.cleaned_data['password1'])


            if user.is_active:
                login(request, user)
                return redirect('chat:index')

        return render(request, self.template_name,
                      {'register_form': register_form})


class Logout(LoginRequiredMixin, View):
    login_url = 'user-profile:login-register'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('user-profile:login-register')

