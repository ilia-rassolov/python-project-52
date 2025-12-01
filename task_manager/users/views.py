from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin

from task_manager.users.forms import SignUpForm
from task_manager.users.models import User

from task_manager.views import (CustomUpdateView,
                               CustomDeleteView)
from task_manager.mixins import CustomUserPassesTestMixin


class UserListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'

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

class UserUpdateView(CustomUserPassesTestMixin, CustomUpdateView):
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

class UserDeleteView(CustomUserPassesTestMixin, CustomDeleteView):
    model = User
    success_url = reverse_lazy('users:index')
    success_message = _('User successfully deleted')
    permission_denied_url = reverse_lazy('users:index')
    permission_denied_message = _("You do not have permission to modify another user.")
    protected_message = _("Cannot delete user because it is in use")
    protected_url = reverse_lazy('users:index')
    context_object_name = 'user'
    extra_context = {
        "title": _("User deletion"),
        "confirmation": _("Are you sure you want to delete")
    }

    def test_func(self):
        return self.request.user == self.get_object()
