from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View


from task_manager.tasks.forms import TaskForm
from task_manager.mixins import CustomLoginMixin, ContextTaskMixin
from task_manager.tasks.models import Task


class TaskListView(ContextTaskMixin, CustomLoginMixin, ListView):
    model = Task
    template_name =  'tasks/index.html'


class CreateTask(ContextTaskMixin, CustomLoginMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks:index')

    # def form_valid(self, form):
    #     form.instance.author = self.request.user  # Установлено текущего пользователя как автора
    #     form.save()
    #     messages.success(
    #         self.request,
    #         'Задача успешно создана'
    #     )
    #     return redirect(self.success_url)

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST or None)
        # form.instance.author = self.request.user
        # print(form['status'])
        if form.is_valid():
            form.save()
            messages.success(
                    request,
                    'Задача успешно создана'
                )
            return redirect('tasks:index')
        return render(request, 'tasks/index.html', {'form': form})


class TaskUpdateView(CustomLoginMixin, UpdateView):
    model = Task
    fields = ['name']
    template_name_suffix = "_update_form"

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        status = Task.objects.get(id=task_id)
        form = TaskForm(request.POST, instance=status)
        form.save()
        messages.success(
            request,
            'Задача успешно изменена'
        )
        return redirect('tasks:index')


class DeleteTask(CustomLoginMixin, DeleteView):
    model = Task
    template_name_suffix = "_delete_form"
    success_url = reverse_lazy('tasks:index')

    def post(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        messages.success(request, 'Задача успешно удалена')
        return redirect('tasks:index')

class TaskDetailView(View):
    pass

    # def get(self, request, *args, **kwargs):
    #     task_id = kwargs.get('pk')
    #     task = get_object_or_404(Task, id=kwargs['id'])
    #     return render(request, '/', context={
    #         'task': task,
    #     })