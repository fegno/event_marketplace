from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from apps.user.views import IndexView,SettingsView

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('settings/', SettingsView.as_view(), name='settings'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here

]
