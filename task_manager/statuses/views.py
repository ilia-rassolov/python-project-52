from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.mixins import CustomLoginMixin


class StatusListView(CustomLoginMixin, ListView):
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'


class CreateStatus(CustomLoginMixin, CreateView):
    form_class = StatusForm
    template_name = 'statuses/create.html'

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=self.request.POST or None)
        form.save()
        messages.success(
                request,
                'Статус успешно создан'
            )
        return redirect('statuses:index')


class StatusUpdateView(CustomLoginMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name_suffix = "_update_form"

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        status = Status.objects.get(id=status_id)
        form = StatusForm(request.POST, instance=status)
        form.save()
        messages.success(
            request,
            'Статус успешно изменен'
        )
        return redirect('statuses:index')


class DeleteStatus(CustomLoginMixin, DeleteView):
    model = Status
    template_name_suffix = "_delete_form"
    success_url = reverse_lazy('statuses:index')

    def post(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        messages.success(request, 'Статус успешно удален')
        return redirect('statuses:index')
