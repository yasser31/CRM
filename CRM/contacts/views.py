import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .forms import NewContactForm, NewCompanyForm, NewDepartementForm
from .models import Company, Departement, Contact
from django.contrib.auth.models import User


@login_required(login_url='/')
def contacts(request):
    ''' get contact page  view '''
    contacts = Contact.objects.filter(user__username=request.user.username)
    context = {
        "contacts": contacts
    }
    return render(request, 'contact.html', context)


@login_required(login_url='/')
def prospects(request):
    ''' get prospects page view '''
    contacts = Contact.objects.filter(client=False,
                                      user__username=request.user.username)
    context = {
        "contacts": contacts
    }
    return render(request, 'contact.html', context)


@login_required(login_url='/')
def clients(request):
    ''' get clients page views '''
    contacts = Contact.objects.filter(client=True,
                                      user__username=request.user.username)
    context = {
        "contacts": contacts
    }
    return render(request, 'contact.html', context)


@login_required(login_url='/')
def add_company(request):
    ''' add company view, use global variable because needed later '''
    if request.method == 'POST':
        request.session["r1"] = request.POST
        form = NewCompanyForm(request.POST)
        if form.is_valid():
            try:
                Company.objects.get(
                    cp_name=request.POST["cp_name"],
                    company_city=request.POST["company_city"],
                    user__username=request.user.username)
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
    r1 = request.session.get("r1")
    ''' add departement view, use global variable because needed later'''
    if request.method == 'POST':
        r2 = request.POST
        request.session['r2'] = request.POST
        form = NewDepartementForm(request.POST)
        if form.is_valid():
            try:
                Departement.objects.get(dep_name=request.POST["dep_name"],
                                        user__username=request.user.username)
            except Departement.DoesNotExist:
                form.save()
                departement = Departement.objects.get(
                    dep_name=request.POST["dep_name"],
                    user__username=request.user.username)
                company = Company.objects.get(
                    cp_name=r1["cp_name"], company_city=r1["company_city"],
                    user__username=request.user.username)
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
def add_contact(request, **kwargs):
    ''' add contact view '''
    if request.method == 'POST':
        r1 = request.session.get("r1")
        r2 = request.session.get("r2")
        form = NewContactForm(request.POST)
        if form.is_valid():
            try:
                Contact.objects.get(
                    name=request.POST["name"],
                    user__username=request.user.username)
            except Contact.DoesNotExist:
                form.save()
                contact = Contact.objects.get(name=request.POST.get("name"))
                company = Company.objects.get(
                    cp_name=r1["cp_name"], company_city=r1["company_city"],
                    user__username=request.user.username)
                departement = Departement.objects.get(dep_name=r2["dep_name"],
                                                      user__username=request.user.username)
                user = User.objects.get(username=request.user.username)
                contact.company = company
                contact.departement = departement
                contact.user = user
                company.user = user
                departement.user = user
                company.save()
                departement.save()
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
    ''' contact detail page '''
    contact = Contact.objects.get(id=contact_id)
    context = {
        "contact": contact
    }
    return render(request, "detail.html", context)


@login_required(login_url='/')
def Set(request, contact_id):
    ''' set prospect to client view '''
    contact = Contact.objects.get(id=contact_id)
    contact.client = True
    contact.save()
    return HttpResponseRedirect("/clients/")


@login_required(login_url='/')
def unset(request, contact_id):
    ''' set client to prospect view '''
    contact = Contact.objects.get(id=contact_id)
    contact.client = False
    contact.save()
    return HttpResponseRedirect("/prospects/")


@login_required(login_url='/')
def client_prospects_percent(request):
    ''' client prospect percent '''
    total_contact = Contact.objects.filter(
        user__username=request.user.username).count()
    total_client = Contact.objects.filter(
        client=True, user__username=request.user.username).count()
    total_prospects = Contact.objects.filter(
        client=False, user__username=request.user.username).count()
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
    ''' contacts per month '''
    year = datetime.date.today().year
    contact_counts_month = []
    client_counts_month = []
    months = ['0' + str(n) if n < 10 else str(n) for n in range(1, 13)]
    for month in months:
        date = str(year) + '-' + month
        contact_count = Contact.objects.filter(
            date__startswith=date, user__username=request.user.username).count()
        contact_counts_month.append(contact_count)
        client_month = Contact.objects.filter(user__username=request.user.username,
                                              date__startswith=date, client=True).count()
        client_counts_month.append(client_month)
    data = {
        "contact": contact_counts_month,
        "client": client_counts_month,
    }
    return JsonResponse(data)


@login_required(login_url='/')
def recent_contact(request):
    ''' recent contacts view, current month '''
    year = datetime.date.today().year
    month = datetime.date.today().month
    if month < 10:
        date = str(year) + "-" + "0" + str(month)
    else:
        date = str(year) + "-" + str(month)
    contact_query = Contact.objects.filter(
        user__username=request.user.username,
        date__startswith=date)[:6]
    contact = [{"name": contact.name, "date": contact.date,
                "function": contact.function,
                "country": contact.country, "city": contact.city,
                "id": contact.id,
                "client": contact.client} for contact in contact_query
               ]
    data = {
        "contact": contact
    }
    return JsonResponse(data)


@login_required(login_url='/')
def thanks(request):
    ''' thanks page view '''
    return render(request, 'thanks.html')


def p_404(request, exception):
    ''' 404 view '''
    return render(request, "404.html", status=404)


def p_500(request):
    ''' 500 view '''
    return render(request, "500.html", status=500)


@login_required(login_url='/')
def edit_comp_get(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    company = Company.objects.get(id=contact.company.id)
    company_id = request.session["cp_id"] = contact.company.id
    dep_id = request.session["dep_id"] = contact.departement.id
    contact_id = request.session["contact_id"] = contact_id
    data = {
        "cp_name": company.cp_name,
        "address": company.address,
        "company_country": company.company_country,
        "company_city": company.company_city,
        "field": company.field,
        "description": company.description
    }
    form = NewCompanyForm(data)
    context = {
        "form": form
    }
    return render(request, "edit_company.html", context)


@login_required(login_url='/')
def edit_comp_post(request):
    cp_id = request.session["cp_id"]
    company = Company.objects.get(id=cp_id)
    form = NewCompanyForm(request.POST)
    if form.is_valid():
        company.cp_name = request.POST["cp_name"]
        company.address = request.POST["address"]
        company.company_country = request.POST["company_country"]
        company.company_city = request.POST["company_city"]
        company.field = request.POST["field"]
        company.description = request.POST["description"]
        company.user = request.user
        company.save()
        return redirect("/edit_dep/")


@login_required(login_url='/')
def edit_departement(request):
    cp_id = request.session["cp_id"]
    company = Company.objects.get(id=cp_id)
    dep_id = request.session.get("dep_id")
    dep = Departement.objects.get(id=dep_id)
    if request.method == "POST":
        form = NewDepartementForm(request.POST)
        if form.is_valid():
            dep.dep_name = request.POST["dep_name"]
            dep.user = request.user
            dep.cp = company
            dep.save()
            return redirect("/edit_contact/")
    else:
        data = {
            "dep_name": dep.dep_name
        }
        form = NewDepartementForm(data)
        context = {
            "form": form
        }
    return render(request, "edit_dep.html", context)


@login_required(login_url='/')
def edit_contact(request):
    c_id = request.session["contact_id"]
    contact = Contact.objects.get(id=c_id)
    if request.method == "POST":
        form = NewContactForm(request.POST)
        if form.is_valid():
            contact.name = request.POST["name"],
            contact.country = request.POST["country"]
            contact.city = request.POST["city"]
            contact.email = request.POST["email"]
            contact.phone_number = request.POST["phone_number"]
            contact.age = request.POST["age"]
            contact.function = request.POST["function"]
            contact.twitter = request.POST["twitter"]
            contact.facebook = request.POST["facebook"]
            contact.linkedin = request.POST["linkedin"]
            if contact.client == "true":
                contact.client = True
            elif contact.client == "false":
                contact.client = False
            else:
                contact.client = contact.client
            contact.user = request.user
            contact.save()
            return redirect("/contact_edited/")
    else:
        data = {
            "name": contact.name,
            "country": contact.country,
            "city": contact.city,
            "email": contact.email,
            "phone_number": contact.phone_number,
            "age": contact.age,
            "function": contact.function,
            "twitter": contact.twitter,
            "facebook": contact.facebook,
            "linkedin": contact.linkedin,
            "client": contact.client
        }
        form = NewContactForm(data)
    context = {
        "form": form
    }
    return render(request, "edit_contact.html", context)


@login_required(login_url='/')
def contact_edited(request):
    return render(request, "contact_edited.html")
