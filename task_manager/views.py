from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .forms import LoginForm


class HomePageView(TemplateView):
    template_name = "home.html"

def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password) # Проверяем учетные данные
            if user is not None:
                login(request, user)     # Выполняем вход
                messages.success(request, 'Вы залогинены')
                return redirect('home')  # Перенаправляем на главную страницу
    return render(request, 'login.html', {'form': form})






