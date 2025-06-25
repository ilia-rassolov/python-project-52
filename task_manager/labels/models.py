from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import ProtectedError


class Label(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.task_set.exists():
            raise ProtectedError(
                _("Cannot delete label because they are being used"),
                self
            )
        super().delete(*args, **kwargs)