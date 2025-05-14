from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.contrib.auth.models import User


from task_manager.users.forms import SignUpForm
from task_manager.users.models import User


class UserListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('signup')

    def post(self, request, *args, **kwargs):
        form = SignUpForm(data=self.request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)  # создание объекта без сохранения в БД
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return redirect('login')
        error_password = "Введенные пароли не совпадают."
        return render(request, 'users/signup.html',
                      {'form': form, 'error_password': error_password})


class UserUpdateView(UpdateView):
    model = User
    template_name = 'auth/user_update_form.html'
    fields = ['first_name', 'last_name', 'username']
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('users:index')

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        form = SignUpForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, 'Пользователь успешно изменен')
            return redirect('users:index')
        error_password = "Введенные пароли не совпадают."
        return render(request, 'auth/user_update_form.html',
                      {
                          'error_password': error_password,
                          'form': form, 'user': user
                      })


class DeleteUser(DeleteView):
    model = User
    template_name = 'auth/user_delete_form.html'
    success_url = reverse_lazy('users:index')

    def post(self, request, *args, **kwargs):
        self.delete(request, *args, **kwargs)
        messages.success(request, 'Пользователь успешно удален')
        return redirect('users:index')
