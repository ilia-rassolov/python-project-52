from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect

from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label

class ContextTaskMixin:
    def get_context_data(self, **kwargs):
        context = kwargs
        context['statuses'] = Status.objects.all()
        context['executors'] = User.objects.all()
        context['labels'] = Label.objects.all()
        context['tasks'] = Task.objects.all()
        return context


class CustomLoginMixin(LoginRequiredMixin):
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,
                'Вы не авторизованы! Пожалуйста, выполните вход.'
            )
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)


