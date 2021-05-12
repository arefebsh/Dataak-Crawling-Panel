from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # post views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    # change and reset password ...
    path('', include('django.contrib.auth.urls')),
    # register
    path('register/', views.register, name='register'),
    # edit profile
    path('edit/', views.edit, name='edit'),

]

