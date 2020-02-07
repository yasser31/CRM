from django.shortcuts import render
from .forms import NewContactForm

def contacts(request):
    return render(request, 'contact.html')

def prospects(request):
    return render(request, 'prospects.html')

def clients(request):
    return render(request, 'clients.html')

def add_contact(request):
    if request.method == 'POST':
        form = NewContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
        else:
            return render(request, NewContactForm(request.POST), 'add_contact.html')
    else:
        return render(request, 'add_contact.html')
