import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from .forms import NewContactForm, NewCompanyForm, NewDepartementForm
from .models import Company, Departement, Contact
from django.contrib.auth.models import User


@login_required(login_url='/')
def contacts(request):
    contacts = Contact.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, 'contact.html', context)


@login_required(login_url='/')
def prospects(request):
    contacts = Contact.objects.filter(client=False)
    context = {
        "contacts": contacts
    }
    return render(request, 'contact.html', context)


@login_required(login_url='/')
def clients(request):
    contacts = Contact.objects.filter(client=True)
    context = {
        "contacts": contacts
    }
    return render(request, 'contact.html', context)


@login_required(login_url='/')
def add_company(request):
    if request.method == 'POST':
        global r1
        r1 = request.POST
        form = NewCompanyForm(request.POST)
        if form.is_valid():
            try:
                Company.objects.get(
                    cp_name=request.POST["cp_name"],
                    company_city=request.POST["company_city"])
            except Company.DoesNotExist:
                form.save()
                return redirect("/add_departement/")
            else:
                return redirect("/add_departement/")
    else:
        form = NewCompanyForm()
    context = {
        "form": form
    }
    return render(request, 'add_company.html', context)


@login_required(login_url='/')
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
                departement = Departement.objects.get(
                    dep_name=request.POST["dep_name"])
                company = Company.objects.get(
                    cp_name=r1["cp_name"], company_city=r1["company_city"])
                departement.cp = company
                departement.save()
                return redirect("/add_contact/")
            else:
                return redirect("/add_contact/")
    else:
        form = NewDepartementForm()
    context = {
        "form": form
    }
    return render(request, 'add_departement.html', context)


@login_required(login_url='/')
def add_contact(request):
    if request.method == 'POST':
        form = NewContactForm(request.POST)
        if form.is_valid():
            try:
                Contact.objects.get(name=request.POST["name"])
            except Contact.DoesNotExist:
                form.save()
                contact = Contact.objects.get(name=request.POST.get("name"))
                company = Company.objects.get(
                    cp_name=r1["cp_name"], company_city=r1["company_city"])
                departement = Departement.objects.get(dep_name=r2["dep_name"])
                user = User.objects.get(username=request.user.username)
                contact.company = company
                contact.departement = departement
                contact.user = user
                contact.save()
                return redirect('/thanks/')
            else:
                pass
    else:
        form = NewContactForm()
    context = {
        "form": form,
    }
    return render(request, 'add_contact.html', context)


@login_required(login_url='/')
def details(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    context = {
        "contact": contact
    }
    return render(request, "detail.html", context)


@login_required(login_url='/')
def Set(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.client = True
    contact.save()
    return HttpResponseRedirect("/clients/")


@login_required(login_url='/')
def unset(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.client = False
    contact.save()
    return HttpResponseRedirect("/prospects/")


@login_required(login_url='/')
def client_prospects_percent(request):
    total_contact = Contact.objects.all().count()
    total_client = Contact.objects.filter(client=True).count()
    total_prospects = Contact.objects.filter(client=False).count()
    try:
        prospects_percent = (total_prospects / total_contact) * 100
    except ZeroDivisionError:
        prospects_percent = 0
    try:
        client_percent = (total_client / total_contact) * 100
    except ZeroDivisionError:
        client_percent = 0
    data = {
        "total_contacts": total_contact,
        "total_clients": total_client,
        "total_prospects": total_prospects,
        "clients_percent": client_percent,
        "prospects_percent": prospects_percent
    }
    return JsonResponse(data)


@login_required(login_url='/')
def contact_month(request):
    year = datetime.date.today().year
    contact_counts_month = []
    client_counts_month = []
    months = ['0' + str(n) if n < 10 else str(n) for n in range(1, 13)]
    for month in months:
        date = str(year) + '-' + month
        contact_count = Contact.objects.filter(date__startswith=date).count()
        contact_counts_month.append(contact_count)
        client_month = Contact.objects.filter(
            date__startswith=date, client=True).count()
        client_counts_month.append(client_month)
    data = {
        "contact": contact_counts_month,
        "client": client_counts_month,
    }
    return JsonResponse(data)


@login_required(login_url='/')
def recent_contact(request):
    year = datetime.date.today().year
    month = datetime.date.today().month
    if month < 10:
        date = str(year) + "-" + "0" + str(month)
    else:
        date = str(year) + "-" + str(month)
    contact_query = Contact.objects.filter(
        date__startswith=date, client=False)[:6]
    client_query = Contact.objects.filter(
        date__startswith=date, client=True)[:6]
    contact = [{"name": contact.name, "date": contact.date,
                "function": contact.function,
                "country": contact.country, "city": contact.city,
                "id": contact.id} for contact in contact_query]
    client = [{"name": contact.name, "date": contact.date,
               "function": contact.function,
               "country": contact.country, "city": contact.city,
               "id": contact.id} for contact in client_query]
    data = {
        "contact": contact,
        "client": client
    }
    return JsonResponse(data)


@login_required(login_url='/')
def thanks(request):
    return render(request, 'thanks.html')
