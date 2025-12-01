from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.views.generic import ListView, DetailView

from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm

from task_manager.views import (CustomCreateView,
                               CustomUpdateView,
                               CustomDeleteView)
from task_manager.mixins import (CustomLoginMixin,
                                 CustomUserPassesTestMixin)


class TaskListView(CustomLoginMixin, ListView):
    model = Task
    template_name =  'tasks/index.html'
    context_object_name = 'tasks'


class TaskCreateView(CustomCreateView):
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

class TaskDetailView(CustomLoginMixin, DetailView):
    template_name = 'tasks/task_detail.html'
    model = Task

class TaskDeleteView(CustomUserPassesTestMixin, CustomDeleteView):
    model = Task
    success_url = reverse_lazy('tasks:index')
    success_message = _('Task successfully deleted')
    permission_denied_url = reverse_lazy('tasks:index')
    permission_denied_message = _("A task can only be deleted by its author.")
    context_object_name = 'task'
    extra_context = {
        "title": _("Task deletion"),
        "confirmation": _("Are you sure you want to delete the task")
    }

    def test_func(self):
        return self.request.user == self.get_object().author
