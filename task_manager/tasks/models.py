from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        verbose_name=_('Name'),
    )
    description = models.TextField(
        max_length=300,
        blank=True,
        verbose_name=_('Description'),
    )
    author = models.ForeignKey(User,
                               on_delete=models.PROTECT,
                               verbose_name=_('Author'),
                               related_name='author',
                               )
    executor = models.ForeignKey(User,
                                 blank=True,
                                 null=True,
                                 on_delete=models.PROTECT,
                                 verbose_name=_('Executor'),
                                 related_name='executor',
                                 )
    status = models.ForeignKey(Status,
                               on_delete=models.PROTECT,
                               verbose_name=_('Status'),
                               )
    labels = models.ManyToManyField(Label,
                                   blank=True,
                                   )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
