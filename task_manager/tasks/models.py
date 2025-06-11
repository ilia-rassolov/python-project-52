from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300, unique=True)
    author = models.ForeignKey(User, related_name='author', on_delete=models.PROTECT)
    executor = models.ForeignKey(User, related_name='executor', on_delete=models.PROTECT)
    status = models.ManyToManyField(Status)
    label = models.ManyToManyField(Label)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name