from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contacts, name="contacts"),
    path('clients/', views.clients, name="clients"),
    path('add_contact/', views.add_contact, name="add_contact"),
    path('add_company/', views.add_company, name="add_company"),
    path('thanks/', views.thanks, name="thanks"),
    path('details/<int:company_id>', views.details, name="details"),
    path('set/<int:contact_id>', views.Set, name="set"),
    path('unset/<int:contact_id>', views.unset, name="unset"),
    path('contact_percent/', views.client_prospects_percent,
         name="contact_percent"),
    path('contact_month/', views.contact_month, name="contact_month"),
    path('recent_contact/', views.recent_contact, name="recent_contact"),
    path('edit_company/<int:contact_id>',
         views.edit_comp_get, name="edit_comp_get"),
    path('edit_company/', views.edit_comp_post, name="edit_comp_post"),
    path('edit_contact/', views.edit_contact, name="edit_contact"),
    path('contact_edited/', views.contact_edited, name="contact_edited"),
    path('delete_contact/<int:contact_id>', views.delete_contact,
         name="delete_contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
