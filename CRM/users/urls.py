from django.urls import path, include
from . import views

urlpatterns = [
    path('registration/', views.registration, name="registration"),
    path("", views.Login, name="Login"),
    path("change_password/", views.change_password, name="change_password"),
    path("accounts/", include('django.contrib.auth.urls'))
]