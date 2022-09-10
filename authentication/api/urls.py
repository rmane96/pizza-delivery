from django.contrib import admin
from django.urls import path, include
from authentication.api.views import register

urlpatterns = [
    path('register/', register.as_view(),name='register'),
]
