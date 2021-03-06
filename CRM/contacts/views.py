import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .forms import NewContactForm, NewCompanyForm
from .models import Company, Contact
from django.contrib.auth.models import User


@login_required(login_url='/')
def contacts(request):
    ''' get contact page  view '''
    contacts = Contact.objects.filter(user__username=request.user.username)
    context = {
        "contacts": contacts
    }
    return render(request, 'contacts/contacts.html', context)


@login_required(login_url='/')
def clients(request):
    ''' get clients page views '''
    clients = Company.objects.filter(
        user__username=request.user.username)
    context = {
        "clients": clients
    }
    return render(request, 'contacts/clients.html', context)


@login_required(login_url='/')
def clients_true(request):
    ''' get customers page views '''
    clients = Company.objects.filter(
        user__username=request.user.username,
        client=True)
    print(clients)
    context = {
        "clients": clients
    }
    return render(request, 'contacts/clients.html', context)


@login_required(login_url='/')
def prospects(request):
    ''' get prospects page views '''
    clients = Company.objects.filter(
        user__username=request.user.username,
        client=False)
    context = {
        "clients": clients
    }
    return render(request, 'contacts/clients.html', context)


@login_required(login_url='/')
def add_client(request):
    ''' add client '''
    if request.method == 'POST':
        form = NewCompanyForm(request.POST)
        if form.is_valid():
            try:
                # check the name and the city of company if it exists
                Company.objects.get(
                    cp_name=form.cleaned_data["cp_name"],
                    company_city=form.cleaned_data["company_city"],
                    user__username=request.user.username)
            except Company.DoesNotExist:
                # if company does not exists we create it
                form.save()
                company = Company.objects.get(
                    cp_name=form.cleaned_data["cp_name"],
                    company_city=form.cleaned_data["company_city"],
                    )
                company.user = request.user
                company.save()
                context = {
                    "company": "added"
                }
                return render(request, "contacts/thanks.html", context)
            else:
                # if client exists we go to next form
                context = {
                    "company": "exists"
                }
                return render(request,
                              "contacts/already_exists.html",
                              context)
    else:
        form = NewCompanyForm()
    context = {
        "form": form
    }
    return render(request, 'contacts/add_client.html', context)


@login_required(login_url='/')
def add_contact(request, company_id):
    ''' add contact view '''
    if request.method == 'POST':
        form = NewContactForm(request.POST, request.FILES)
        if form.is_valid():
            # check if contact exists
            try:
                Contact.objects.get(
                    name=form.cleaned_data["name"],
                    user__username=request.user.username,
                    email=form.cleaned_data["email"])
            # if contact does not exists we create it
            except Contact.DoesNotExist:
                form.save()
                context = {
                    "contact": "added"
                }
                return render(request, 'contacts/thanks.html',
                              context)
            else:
                # if contact exists we redirect to this page
                context = {
                    "contact": "exists"
                }
                return render(request,
                              "contacts/already_exists.html",
                              context)
    else:
        form = NewContactForm(username=request.user.username,
                              company_id=company_id)
    context = {
        "form": form,
    }
    return render(request, 'contacts/add_contact.html', context)


@login_required(login_url='/')
def client_details(request, company_id):
    ''' contact detail page '''
    company = Company.objects.get(id=company_id)
    contacts = Contact.objects.filter(
        user__username=request.user.username,
        company__id=company_id)
    context = {
        "company": company,
        "contacts": contacts
    }
    return render(request, "contacts/client_detail.html", context)


@login_required(login_url='/')
def Set(request, company_id):
    ''' set prospect to client view '''
    company = Company.objects.get(id=company_id)
    if company.client is True:
        company.client = False
    elif company.client is False:
        company.client = True
    company.save()
    data = {
        "client": company.client
    }
    return JsonResponse(data)


@login_required(login_url='/')
def client_prospects_percent(request):
    ''' client prospect percent '''
    total_companies = Company.objects.filter(
        user__username=request.user.username).count()
    total_clients = Company.objects.filter(
        client=True, user__username=request.user.username).count()
    total_prospects = Company.objects.filter(
        client=False, user__username=request.user.username).count()
    try:
        prospects_percent = (total_prospects / total_companies) * 100
    except ZeroDivisionError:
        prospects_percent = 0
    try:
        client_percent = (total_clients / total_companies) * 100
    except ZeroDivisionError:
        client_percent = 0
    data = {
        "total_companies": total_companies,
        "total_clients": total_clients,
        "total_prospects": total_prospects,
        "clients_percent": client_percent,
        "prospects_percent": prospects_percent
    }
    return JsonResponse(data)


@login_required(login_url='/')
def contact_month(request):
    ''' contacts per month '''
    year = datetime.date.today().year
    contact_counts_month = []
    username = request.user.username
    months = ['0' + str(n) if n < 10 else str(n) for n in range(1, 13)]
    for month in months:
        date = str(year) + '-' + month
        contact_count = Contact.objects.filter(
            date__startswith=date,
            user__username=request.user.username).count()
        contact_counts_month.append(contact_count)
    data = {
        "contact": contact_counts_month,
    }
    return JsonResponse(data)


@login_required(login_url='/')
def thanks(request):
    ''' thanks page view '''
    return render(request, 'contacts/thanks.html')


def p_404(request, exception):
    ''' 404 view '''
    return render(request, "404.html", status=404)


def p_500(request):
    ''' 500 view '''
    return render(request, "500.html", status=500)


@login_required(login_url='/')
def edit_comp(request, company_id):
    company = Company.objects.get(id=company_id)
    if request.method == "POST":
        form = NewCompanyForm(request.POST)
        if form.is_valid():
            company.cp_name = form.cleaned_data["cp_name"]
            company.address = form.cleaned_data["address"]
            company.company_country = form.cleaned_data["company_country"]
            company.company_city = form.cleaned_data["company_city"]
            company.field = form.cleaned_data["field"]
            company.description = form.cleaned_data["description"]
            company.email = form.cleaned_data["email"]
            company.phone_number = form.cleaned_data["phone_number"]
            company.user = request.user
            if form.cleaned_data["client"] == 'true':
                company.client = True
            else:
                company.client = False
            company.save()
            context = {
                "company": "edited"
            }
            return render(request, "contacts/edition_done.html",
                          context)
    else:
        data = {
            "cp_name": company.cp_name,
            "address": company.address,
            "company_country": company.company_country,
            "company_city": company.company_city,
            "field": company.field,
            "description": company.description,
            "client": company.client,
            "email": company.email,
            "phone_number": company.phone_number
        }
        form = NewCompanyForm(data)
    context = {
        "form": form
    }
    return render(request, "contacts/edit_client.html", context)


@login_required(login_url='/')
def edit_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    request.session["c_id"] = contact.id
    if request.method == "POST":
        form = NewContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact.name = form.cleaned_data["name"]
            contact.country = form.cleaned_data["country"]
            contact.city = form.cleaned_data["city"]
            contact.email = form.cleaned_data["email"]
            contact.phone_number = form.cleaned_data["phone_number"]
            contact.age = form.cleaned_data["age"]
            contact.dep_name = form.cleaned_data["dep_name"]
            contact.function = form.cleaned_data["function"]
            if "photo" in form.cleaned_data:
                contact.photo = form.cleaned_data["photo"]
            contact.user = request.user
            contact.save()
            context = {
                "contact": 'edited'
            }
            return render(request,
                          "contacts/edition_done.html",
                          context)
    else:
        data = {
            "name": contact.name,
            "country": contact.country,
            "city": contact.city,
            "email": contact.email,
            "phone_number": contact.phone_number,
            "age": contact.age,
            "dep_name": contact.dep_name,
            "function": contact.function,
            "photo": contact.photo.url
        }
        form = NewContactForm(data,
                              username=request.user.username,
                              company_id=contact.company.id)
    context = {
        "form": form
    }
    return render(request, "contacts/edit_contact.html", context)


@login_required(login_url='/')
def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    context = {
        "contact": "deleted"
    }
    return render(request, "contacts/deletion_done.html",
                  context)


@login_required(login_url='/')
def delete_company(request, company_id):
    company = Company.objects.get(id=company_id)
    company.delete()
    context = {
        "company": "deleted"
    }
    return render(request, "contacts/deletion_done.html",
                  context)
