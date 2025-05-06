from django.urls import path
from task_manager.user import views


urlpatterns = [
    path('', views.UserListView.as_view(), name='index'),
    path('create/', views.SignUp.as_view(), name='signup'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteUser.as_view(), name='delete'),
]