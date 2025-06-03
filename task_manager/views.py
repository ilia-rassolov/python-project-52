from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm

from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = "home.html"


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=self.request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,
                                password=password)
            if user is not None:
                login(self.request, user)
                messages.add_message(self.request, messages.SUCCESS,
                                     _("You are logged in"))
                return redirect('home')
        error_password =\
            ("Пожалуйста, введите правильные имя пользователя и пароль."
             " Оба поля могут быть чувствительны к регистру.")
        return render(request, 'login.html',
                      {'error_password': error_password})


class Logout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.INFO,
                             "Вы разлогинены")
        logout(request)
        return redirect('home')
