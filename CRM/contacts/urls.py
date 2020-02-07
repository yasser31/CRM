from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contacts, name="contacts"),
    path('prospects/', views.prospects, name="prospects"),
    path('clients/', views.clients, name="clients"),
    path('add_contact/', views.add_contact, name="add_contact"),
    path('thanks/', views.thanks, name="thanks"),
    path('details/<int:contact_id>', views.details, name="details"),
    path('set/<int:contact_id>', views.Set, name="set"),
    path('unset/<int:contact_id>', views.unset, name="unset"),
]