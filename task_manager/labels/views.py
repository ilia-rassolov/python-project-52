from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
from task_manager.mixins import CustomLoginMixin


class LabelListView(CustomLoginMixin, ListView):
    model = Label
    template_name = 'labels/index.html'
    context_object_name = 'labels'


class CreateLabel(CustomLoginMixin, CreateView):
    form_class = LabelForm
    template_name = 'labels/create.html'

    def post(self, request, *args, **kwargs):
        form = LabelForm(data=self.request.POST or None)
        form.save()
        messages.success(
                request,
                'Метка успешно создана'
            )
        return redirect('labels:index')


class LabelUpdateView(CustomLoginMixin, UpdateView):
    model = Label
    fields = ['name']
    template_name_suffix = "_update_form"

    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        label = Label.objects.get(id=label_id)
        form = LabelForm(request.POST, instance=label)
        form.save()
        messages.success(
            request,
            'Метка успешно изменена'
        )
        return redirect('labels:index')


class DeleteLabel(CustomLoginMixin, DeleteView):
    model = Label
    template_name_suffix = "_delete_form"
    success_url = reverse_lazy('labels:index')

    def post(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        messages.success(request, 'Метка успешно удалена')
        return redirect('labels:index')
