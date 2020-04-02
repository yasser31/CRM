from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registration/', views.registration, name="registration"),
    path("", views.Login, name="Login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("change_password/", views.change_password, name="change_password"),
    path("change_done/", views.password_change_done, name="change_done"),
]
