from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from task_manager.users.models import User

# Отменяем регистрацию стандартной модели User
# admin.site.unregister(User)


# Создаём кастомный класс админки
@admin.register(User)
class CustomUserAdmin(DefaultUserAdmin):
    list_display = ('username',
                    'first_name',
                    'last_name',
                    'date_joined',
                    'is_staff')  # Настраиваем отображаемые поля
    search_fields = ('username',
                     'first_name',
                     'last_name',
                     'date_joined')  # Поля для поиска
    list_filter = ('is_staff',
                   'is_superuser',
                   'is_active')  # Поля для фильтрации
