from django import forms # Импортируем формы Django

from task_manager.user.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']