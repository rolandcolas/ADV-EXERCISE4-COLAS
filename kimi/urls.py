# kimi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('tags/', views.tag_list, name='tag-list'),
     path('categories/', views.category_list),
]
