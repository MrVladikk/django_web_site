from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "forum"
urlpatterns = [
    path("", views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # маршрут для логина
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # маршрут для выхода
    path("register/", views.register, name="register"),
    path('profile/', views.profile, name='profile'),
    path('login/', views.auth, name='auth'),
]
