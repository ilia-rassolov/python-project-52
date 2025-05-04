from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignUpForm


class UserListView(ListView):
    model = User
    template_name = 'user/index.html'
    context_object_name = 'users'


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'user/signup.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = SignUpForm(data=self.request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)  # создание объекта без сохранения в БД
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return redirect('home')
        error_password = "Введенные пароли не совпадают."
        return render(request, 'user/signup.html', {'form': form, 'error_password': error_password})


class UpdateUser(UpdateView):
    model = User
    template_name = 'users/update.html'
    fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = SignUpForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, 'Пользователь успешно изменен')
            return redirect('index')
        error_password = "Введенные пароли не совпадают."
        return render(request, 'update.html',
                      {'error_password': error_password, 'form': form, 'user': user})


# class DeleteUser(UpdateView):
#     model = User
#     template_name = 'users/update.html'
#     fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
#     success_url = reverse_lazy('index')



