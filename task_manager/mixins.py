from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.db.models import ProtectedError

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin


class CustomLoginMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,
                _("You are not logged in! Please sign in.")
            )
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)


class CustomCreateView(CustomLoginMixin, SuccessMessageMixin, CreateView):  #replace
    template_name = 'create_update_form.html'


class CustomUpdateView(CustomLoginMixin, SuccessMessageMixin, UpdateView):
    template_name = 'create_update_form.html'


class CustomDeleteView(CustomLoginMixin, SuccessMessageMixin, DeleteView):
    template_name = 'delete_form.html'
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)








