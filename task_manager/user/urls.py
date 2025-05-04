from django.urls import path
from task_manager.user import views


urlpatterns = [
    path('', views.UserListView.as_view(), name='index'),
    path('create/', views.SignUp.as_view(), name='signup'),
    path('<int:pk>/update/', views.UpdateUser.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]