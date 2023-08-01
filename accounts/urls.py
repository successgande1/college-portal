from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', auth_view.LoginView.as_view(template_name='accounts/login.html'), name = 'user_login'),

]

