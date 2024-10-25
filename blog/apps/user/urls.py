# blog/apps/user/urls.py
from django.urls import path
import apps.user.views as views
from .views import AboutView, ContactView


app_name = 'user'

urlpatterns = [
    path('user/profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('auth/register/', views.RegisterView.as_view(), name='auth_register'),
    path('auth/login/', views.LoginView.as_view(), name='auth_login'),
    path('auth/logout/', views.LogoutView.as_view(), name='auth_logout'),
    path('user/about/', AboutView.as_view(), name='about'),
    path('user/contact/', ContactView.as_view(), name='contact'),
]
