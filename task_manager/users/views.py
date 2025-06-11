from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin


from task_manager.users.forms import SignUpForm
from task_manager.users.models import User


class UserListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('signup')

    def post(self, request, *args, **kwargs):
        form = SignUpForm(data=self.request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(
                request,
                'Пользователь успешно зарегистрирован'
            )
            return redirect('login')
        error_password = "Введенные пароли не совпадают."
        return render(
            request,
            'users/create.html',
            {'form': form, 'error_password': error_password}
        )


class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name_suffix = "_update_form"
    login_url = "users"

    def test_func(self):
        return self.request.user.id == self.kwargs.get('pk')

    def handle_no_permission(self):
        if self.raise_exception:
            raise self.get_permission_denied_message()
        messages.error(
            self.request,
            'У вас нет прав для изменения другого пользователя.'
        )
        return redirect('users:index')

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
        return render(request, 'users/users_update_form.html',
                      {
                          'error_password': error_password,
                          'form': form, 'user': user
                      })


class DeleteUser(UserPassesTestMixin, DeleteView):
    model = User
    template_name_suffix = "_delete_form"
    success_url = reverse_lazy('users:index')

    def test_func(self):
        return self.request.user.id == self.kwargs.get('pk')

    def handle_no_permission(self):
        if self.raise_exception:
            raise self.get_permission_denied_message()
        messages.error(
            self.request,
            'У вас нет прав для изменения другого пользователя.'
        )
        return redirect('users:index')

    def post(self, request, *args, **kwargs):
        self.delete(request, *args, **kwargs)
        messages.success(request, 'Пользователь успешно удален')
        return redirect('users:index')
