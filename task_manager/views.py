from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
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
            user = authenticate(username=username, password=password) # Проверяем учетные данные
            if user is not None:
                login(self.request, user)     # Выполняем вход
                messages.add_message(self.request, messages.SUCCESS, "Вы залогинены")
                return redirect('home')  # Перенаправляем на главную страницу
        error_password = "Пожалуйста, введите правильные имя пользователя и пароль. Оба поля могут быть чувствительны к регистру."
        return render(request, 'login.html', {'error_password': error_password})







