from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin


class CustomLoginMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,
                _("You are not logged in! Please sign in.")
            )
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)

class CustomSingleObjectMixin(SingleObjectMixin):
    context_object_name = None

class CustomUserPassesTestMixin(UserPassesTestMixin):
    permission_denied_url = None
    permission_denied_message = None

    def handle_no_permission(self):
        messages.error(
            self.request,
            self.permission_denied_message
        )
        return redirect(self.permission_denied_url)













