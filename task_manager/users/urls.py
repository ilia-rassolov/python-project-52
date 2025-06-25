from django.urls import path
from task_manager.users import views


app_name = "users"
urlpatterns = [
    path('', views.UserListView.as_view(), name='index'),
    path('create/', views.SignUp.as_view(), name='signup'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='delete'),
]
