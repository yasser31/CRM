from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewContactForm
from .models import Contact

def contacts(request):
    contacts = Contact.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, 'contact.html', context)

def prospects(request):
    contacts = Contact.objects.filter(client=False)
    context = {
        "contacts": contacts
    }
    return render(request, 'contact.html', context)

def clients(request):
    contacts = Contact.objects.filter(client=True)
    context = {
        "contacts": contacts
    }
    return render(request, 'contact.html', context)

def add_contact(request):
    print(request.POST)
    if request.method == 'POST':
        form = NewContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
        
    
    return render(request, 'add_contact.html')

def details(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    context = {
        "contact": contact
    }
    return render(request, "detail.html", context)

def Set(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.client=True
    contact.save()
    return HttpResponseRedirect("/clients/")

def unset(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.client=False
    contact.save()
    return HttpResponseRedirect("/prospects/")

def thanks(request):
    return render(request, 'thanks.html')