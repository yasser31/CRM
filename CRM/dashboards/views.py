from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/')
def dashboard(request):
    ''' get dashbord page '''
    return render(request, 'dashboard.html')
