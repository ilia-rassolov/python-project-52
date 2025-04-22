from django.urls import path
from task_manager.user import views
from task_manager.user.views import (IndexView)


urlpatterns = [
    path('', IndexView.as_view(), name='users_index'),
    # path('<int:id>/', ArticleView.as_view(), name='show_article',),
    # path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    # path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name='articles_delete'),
    # path('<int:id>/', CommentArticleView.as_view(), name='comment_create',),
    # path('<int:article_id>/comments/<int:id>/', ArticleCommentsView.as_view()),
]