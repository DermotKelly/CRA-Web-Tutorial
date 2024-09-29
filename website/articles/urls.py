from django.urls import path
from . import views



urlpatterns = [
    path('', views.articles, name='articles'),
    path('article/<str:pk>/', views.article, name='article'),
    path('create-article/', views.createArticle, name='create-article')
]



