from django.contrib import admin
from django.urls import path, include
from .views import home, user_profile_view

urlpatterns = [
    path('', home, name="home"),
    path('profile/', user_profile_view, name='user_profile'),
]