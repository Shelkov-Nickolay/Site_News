from django.urls import path
from .views import (PostList, PostDetail, NewsCreate,
                    Search, ArticlesCreate, NewsUpdate,
                    ArticlesUpdate, NewsDelete, ArticlesDelete, subscriptions
                    )
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('news/', cache_page(60)(PostList.as_view()), name='post_list'),
    path('search/', cache_page(60)(Search.as_view())),
    path('news/<int:pk>', cache_page(60*5)(PostDetail.as_view()), name='post_detail'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
    path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('articles/<int:pk>/update/', ArticlesUpdate.as_view(), name='articles_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
]
