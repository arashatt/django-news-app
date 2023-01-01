from django.contrib import admin
from django.urls import path
from .views import NewsListView
from .views import NewsDetailView
from .views import NewsTopicsView 

urlpatterns = [
    path('', NewsTopicsView.as_view(), name='news-topics'),
    path('<str:topic>', NewsListView.as_view(), name='news-list'),
    path('<str:topic>/<slug:slug>', NewsDetailView.as_view(), name='news-detail'),
]
