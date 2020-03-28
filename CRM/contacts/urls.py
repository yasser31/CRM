from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
     path('contacts/', views.contacts, name="contacts"),
     path('clients/', views.clients, name="clients"),
     path('add_contact/<int:company_id>', views.add_contact,
          name="add_contact"),
     path('add_client/', views.add_client, name="add_client"),
     path('thanks/', views.thanks, name="thanks"),
     path('details/<int:company_id>', views.client_details,
          name="client_details"),
     path('set/<int:company_id>', views.Set, name="set"),
     path('contact_percent/', views.client_prospects_percent,
          name="contact_percent"),
     path('contact_month/', views.contact_month, name="contact_month"),
     path('edit_company/<int:company_id>',
          views.edit_comp, name="edit_comp"),
     path('edit_contact/<int:contact_id>', views.edit_contact,
          name="edit_contact"),
     path('delete_contact/<int:contact_id>', views.delete_contact,
          name="delete_contact"),
     path('delete_company/<int:company_id>', views.delete_company,
          name="delete_company"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
