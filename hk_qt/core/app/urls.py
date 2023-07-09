from django.contrib.auth import views as auth_views
from django.urls import path

from core.app import forms, views

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="auth/login.html", form_class=forms.LoginForm
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="auth/logged_out.html"),
        name="logout",
    ),
    path("register/", views.CreateUserView.as_view(), name="register"),
    path("calculate/", views.calculate, name="calculate"),
    path("", views.index, name="home"),
]
