from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import NewContactForm, NewCompanyForm, NewDepartementForm
from .models import Company, Departement, Contact
from django.contrib.auth.models import User


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
                Company.objects.get(cp_name=request.POST["cp_name"], company_city=request.POST["company_city"])
            except Company.DoesNotExist:
                form.save()
            else:
                pass
        else:
            print(form.errors)
    form = NewCompanyForm()
    context = {
        "form1" : form
    }
    return render(request, 'add_contact.html', context)

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
                company = Company.objects.get(cp_name=r1["cp_name"], company_city=r1["company_city"])
                departement.cp = company
                departement.save()
            else:
                pass
    form = NewDepartementForm()
    context = {
        "form2" : form
    }      
    return render(request, 'add_contact.html', context)


def add_contact(request):
    if request.method == 'POST':
        form = NewContactForm(request.POST)
        if form.is_valid():
            try:
                Contact.objects.get(name=request.POST["name"])
            except Contact.DoesNotExist:
                form.save()
                contact = Contact.objects.get(name=request.POST.get("name"))
                company = Company.objects.get(cp_name=r1["cp_name"], company_city=r1["company_city"])
                departement = Departement.objects.get(dep_name=r2["dep_name"])
                user = User.objects.get(username=request.user.username)
                contact.company = company
                contact.departement = departement
                contact.user = user
                contact.save()
                return HttpResponseRedirect('/thanks/')
            else:
                pass
    form = NewContactForm()
    context = {
        "form" : form
    }
    return render(request, 'add_contact.html', context)

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

def client_prospects_percent(request):
    total_contact = Contact.objects.all().count()
    total_client= Contact.objects.filter(client=True).count()
    total_prospects = Contact.objects.filter(client=False).count()
    prospects_percent = (total_prospects * total_client)/100
    client_percent = (total_client * total_contact) / 100
    data = {
        "total_contact" : total_contact,
        "total_client" : total_client,
        "total_prospects" : total_prospects,
        "client_percent" : client_percent,
        "prospects_percent" : prospects_percent
    }
    return JsonResponse(data)

def contact_month(request):
    contact_counts_month = []
    client_counts_month = []
    months = ('January', 'February', 'March', 'April', 'May',
              'June', 'July', 'August', 'September', 'October', 
              'November', 'December')
    for month in months:
        contact_count = Contact.objects.filter(date=month).count()
        contact_counts_month.append(contact_count)
        client_month = Contact.objects.filter(date=month, client=True).count()
        client_counts_month.append(client_month)
        data = {
            "contact" : contact_counts_month,
            "client" : contact_counts_month
        }
        return JsonResponse(data)

def thanks(request):
    return render(request, 'thanks.html')