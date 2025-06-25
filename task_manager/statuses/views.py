from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.views.generic import ListView

from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.mixins import (CustomLoginMixin,
                                 CustomCreateView,
                                 CustomUpdateView,
                                 CustomDeleteView,
                                 )


class StatusListView(CustomLoginMixin, ListView):
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'

class StatusCreateView(CustomCreateView):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses:index')
    success_message = _("Status successfully created")
    extra_context = {
        "button_name": _("Create"),
        "header": _("Create a status")
    }

class StatusUpdateView(CustomUpdateView):
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses:index')
    success_message = _("The status successfully updated")
    extra_context = {
        "button_name": _("Update"),
        "header": _("Update status")
    }


class StatusDeleteView(CustomDeleteView):
    model = Status
    success_url = reverse_lazy('statuses:index')
    success_message = _('Status successfully deleted')
    protected_message = _("Cannot delete a status because it is in use")
    protected_url = reverse_lazy('statuses:index')
    extra_context = {
        "title": _("Status deletion"),
        "confirmation": _("Are you sure you want to delete the status")
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_to_delete'] = self.get_object()
        return context
