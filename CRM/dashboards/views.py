from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/')
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url='/')
def handler404(request, exception):
    return render(request, '404.html', status=404)


@login_required(login_url='/')
def handler500(request):
    return render(request, '500.html', status=500)
