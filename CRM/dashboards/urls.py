from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),

]

handler404 = views.handler404
handler500 = views.handler500
