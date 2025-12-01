from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.views.generic import ListView

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label

from task_manager.mixins import CustomLoginMixin
from task_manager.views import (CustomCreateView,
                               CustomUpdateView,
                               CustomDeleteView)


class LabelListView(CustomLoginMixin, ListView):
    model = Label
    template_name = 'labels/index.html'
    context_object_name = 'labels'

class LabelCreateView(CustomCreateView):
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels:index')
    success_message = _("Label successfully created")
    extra_context = {
        "button_name": _("Create"),
        "header": _("Create a label")
    }

class LabelUpdateView(CustomUpdateView):
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels:index')
    success_message = _("The label successfully updated")
    extra_context = {
        "button_name": _("Update"),
        "header": _("Update label")
    }

class LabelDeleteView(CustomDeleteView):
    model = Label
    success_url = reverse_lazy('labels:index')
    success_message = _('Label successfully deleted')
    protected_message = _("Cannot delete a label because it is in use")
    protected_url = reverse_lazy('labels:index')
    context_object_name = 'label'
    extra_context = {
        "title": _("Label deletion"),
        "confirmation": _("Are you sure you want to delete the label")
    }
