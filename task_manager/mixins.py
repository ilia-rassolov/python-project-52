from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect


class CustomLoginMixin(LoginRequiredMixin):
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                self.request,
                'У вас нет прав для изменения другого пользователя.'
            )
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)
