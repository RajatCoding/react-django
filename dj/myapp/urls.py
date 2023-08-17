from django.contrib import admin
from django.urls import path, include
from . import api

urlpatterns = [
  
    path('', api.UserListView.as_view()),
    
]