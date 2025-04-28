from django.urls import path
from task_manager.user import views


urlpatterns = [
    path('', views.UserListView.as_view(), name='user-list'),
    path('create/', views.signup, name='signup'),
    # path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    # path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name='articles_delete'),
    # path('<int:id>/', CommentArticleView.as_view(), name='comment_create',),
    # path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
]