from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contacts, name="contacts"),
    path('prospects/', views.prospects, name="prospects"),
    path('clients/', views.clients, name="clients"),
    path('add_contact/', views.add_contact, name="add_contact"),
    path('thanks/', views.thanks, name="thanks")
    
]