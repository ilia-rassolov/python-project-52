from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name

