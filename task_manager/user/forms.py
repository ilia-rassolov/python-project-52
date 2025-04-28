from django import forms # Импортируем формы Django
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'password']

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=200, help_text='Required')

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')


