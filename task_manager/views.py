from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm

from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import ProtectedError

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView

from task_manager.mixins import CustomLoginMixin, CustomSingleObjectMixin



class HomePageView(TemplateView):
    template_name = "home.html"


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = 'create_update_form.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    success_message = _('You are logged in')
    extra_context = {
        'header': _('Log In'),
        'button_name': _('Login'),
    }


class Logout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, _("You are logged out"))
        logout(request)
        return redirect('home')

class CustomCreateView(CustomLoginMixin, SuccessMessageMixin, CreateView):  #replace
    template_name = 'create_update_form.html'


class CustomUpdateView(CustomLoginMixin, SuccessMessageMixin, UpdateView):
    template_name = 'create_update_form.html'


class CustomDeleteView(CustomLoginMixin,
                       CustomSingleObjectMixin,
                       SuccessMessageMixin,
                       DeleteView):
    template_name = 'delete_form.html'
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)
