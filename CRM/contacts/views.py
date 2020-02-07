from django.shortcuts import render


def contacts(request):
    return render(request, 'contact.html')

def prospects(request):
    return render(request, 'prospects.html')

def clients(request):
    return render(request, 'clients.html')

def add_contact(request):
    return render(request, 'add_contact.html')
