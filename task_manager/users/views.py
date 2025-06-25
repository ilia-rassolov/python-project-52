from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


from task_manager.users.forms import SignUpForm
from task_manager.users.models import User

from task_manager.mixins import (CustomLoginMixin,
                                 CustomCreateView,
                                 CustomUpdateView,
                                 CustomDeleteView
                                 )


class UserListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'


# class SignUp(SuccessMessageMixin, CreateView):
#     form_class = SignUpForm
#     template_name = 'create_update_form.html'
#     success_url = reverse_lazy('login')
#     success_message = _("User registered successfully")
#     extra_context = {
#         "button_name": _("Register"),
#         "header": _("Registration")
#     }

class SignUp(SuccessMessageMixin, CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'create_update_form.html'
    success_url = reverse_lazy('login')
    success_message = _("User registered successfully")
    extra_context = {
        "button_name": _("Register"),
        "header": _("Registration")
    }

# class UserUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
#     model = User
#     redirect_field_name = 'users:index'
#     form_class = SignUpForm
#     template_name = 'create_update_form.html'
#     success_url = reverse_lazy('users:index')
#     success_message = _("User successfully changed")
#     permission_denied_url = reverse_lazy('users:index')
#     permission_denied_message = 'You do not have permission to modify another user.'
#     extra_context = {
#         "button_name": _("Change"),
#         "header": _("Change user")
#     }
#
#     def test_func(self):
#         return self.request.user.id == self.kwargs.get('pk')
#
#     def handle_no_permission(self):
#         messages.error(
#             self.request,
#             _(self.permission_denied_message)
#         )
#         return redirect(self.success_url)

class UserUpdateView(UserPassesTestMixin, CustomUpdateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('users:index')
    success_message = _("User successfully changed")
    permission_denied_url = reverse_lazy('users:index')
    permission_denied_message = _("You do not have permission to modify another user.")
    extra_context = {
        "button_name": _("Update"),
        "header": _("Update user")
    }

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        messages.error(
            self.request,
            self.permission_denied_message
        )
        return redirect(self.permission_denied_url)

class CustomUserPassesTestMixin(UserPassesTestMixin):
    pass

# class DeleteUser(CustomLoginMixin, UserPassesTestMixin, DeleteView):
#     model = User
#     template_name_suffix = "_delete_form"
#     success_url = reverse_lazy('users:index')
#
#     def test_func(self):
#         return self.request.user.id == self.kwargs.get('pk')
#
#     def handle_no_permission(self):
#         messages.error(
#             self.request,
#             _("You do not have permission to modify another user.")
#         )
#         return redirect('users:index')
#
#     def post(self, request, *args, **kwargs):
#         self.delete(request, *args, **kwargs)
#         messages.success(request, _("User successfully deleted"))
#         return redirect('users:index')

class UserDeleteView(UserPassesTestMixin, CustomDeleteView):
    model = User
    success_url = reverse_lazy('users:index')
    success_message = _('User successfully deleted')
    permission_denied_url = reverse_lazy('users:index')
    permission_denied_message = _("You do not have permission to modify another user.")
    protected_message = _("Cannot delete user because it is in use")
    protected_url = reverse_lazy('users:index')
    extra_context = {
        "title": _("User deletion"),
        "confirmation": _("Are you sure you want to delete the users")
    }

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        messages.error(
            self.request,
            self.permission_denied_message
        )
        return redirect(self.permission_denied_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_to_delete'] = self.get_object()
        return context
