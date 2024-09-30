# kimi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('tags/', views.tag_list, name='tag-list'),  # Endpoint for your tag API
]
