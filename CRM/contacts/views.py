from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewContactForm, NewCompanyForm, NewDepartementForm
from .models import Company, Departement, Contact

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


def add_company(request):
    if request.method == 'POST':
        global r1
        r1 = request.POST
        form = NewCompanyForm(request.POST)
        if form.is_valid():
            try:
                Company.objects.get(cp_name=request.POST["cp_name"], city=request.POST["company_city"])
            except Company.DoesNotExist:
                form.save()
            else:
                pass
        else:
            print(form.errors)   
    return render(request, 'add_contact.html')

def add_departement(request):
    if request.method == 'POST':
        global r2
        r2 = request.POST
        form = NewDepartementForm(request.POST)
        if form.is_valid():
            try:
                Departement.objects.get(dep_name=request.POST["dep_name"])
            except Departement.DoesNotExist:
                form.save()
                departement = Departement.objects.get(dep_name=request.POST["dep_name"])
                company = Company.objects.get(cp_name=r1["cp_name"], city=r1["company_city"])
                departement.cp = company
                departement.save()
            else:
                pass
            
    return render(request, 'add_contact.html')


def add_contact(request):
    if request.method == 'POST':
        form = NewContactForm(request.POST)
        if form.is_valid():
            try:
                Contact.objects.get(name=request.POST["name"])
            except Contact.DoesNotExist:
                form.save()
                contact = Contact.objects.get(name=request.POST.get("name"))
                company = company = Company.objects.get(cp_name=r1["cp_name"], city=r1["company_city"])
                departement = Departement.objects.get(dep_nam=r2["dep_name"])
                contact.company = company
                contact.departement = departement
                contact.save()
            else:
                pass
        else:
            print(form.errors)
            
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