from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registration/', views.registration, name="registration"),
    path("", views.Login, name="Login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("change_password/", views.change_password, name="change_password"),
    path("change_done/", views.password_change_done, name="change_done"),
    path("password_reset/",
         auth_views.PasswordResetView.as_view(
             template_name="registration/password_reset.html",
             success_url="/password_reset_done/"),
         name="password_reset"),
    path("password_reset_done/",
         auth_views.PasswordResetDoneView.as_view(
             template_name="registration/password_reset_done.html"),
         name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(
             template_name="registration/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path("password_reset_complete/",
         auth_views.PasswordResetCompleteView.as_view(
             template_name="registration/password_reset_complete.html"),
         name="password_reset_complete")
]
