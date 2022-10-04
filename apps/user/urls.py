from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from apps.user.views import IndexView

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login')
]
