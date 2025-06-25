from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin

from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
from task_manager.mixins import (CustomLoginMixin,
                                 CustomCreateView,
                                 CustomUpdateView,
                                 CustomDeleteView
                                 )


class TaskListView(CustomLoginMixin, ListView):
    model = Task
    template_name =  'tasks/index.html'
    context_object_name = 'tasks'


class TaskCreateView(CustomCreateView):           # dooble task and others
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:index')
    success_message = _("Task successfully created")
    extra_context = {
        "button_name": _("Create"),
        "header": _("Create a task")
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(CustomUpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:index')
    success_message = _("Task successfully updated")
    extra_context = {
        "button_name": _("Update"),
        "header": _("Update task")
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskDeleteView(UserPassesTestMixin, CustomDeleteView):
    model = Task
    success_url = reverse_lazy('tasks:index')
    success_message = _('Task successfully deleted')
    permission_denied_url = reverse_lazy('tasks:index')
    permission_denied_message = _("A task can only be deleted by its author.")
    extra_context = {
        "title": _("Task deletion"),
        "confirmation": _("Are you sure you want to delete the task")
    }

    def test_func(self):
        return self.request.user == self.get_object().author

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

class TaskDetailView(CustomLoginMixin, DetailView):
    pass

