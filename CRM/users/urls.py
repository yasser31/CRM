from django.urls import path, include
from . import views

urlpatterns = [
    path('registration/', views.registration, name="registration"),
    path("", views.Login, name="Login"),
    path("accounts/", include('django.contrib.auth.urls'))
]