from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'password') # Перечисляем поля, отображаемые в таблице списка пользователей
    search_fields = ['first_name', 'last_name', 'created_at']
    list_filter = (('created_at', DateFieldListFilter),) # Перечисляем поля для фильтрации