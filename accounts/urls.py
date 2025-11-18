from django.urls import path
from . views import *
from django.contrib.auth import views as auth_views
from . forms import LoginForm


urlpatterns = [
    path('', register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(authentication_form=LoginForm, template_name = 'login.html'), name='login'),
    path('logout', logout, name='logout'),
    path('profile/', profile_view, name='profile'),
]
