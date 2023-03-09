from django.shortcuts import render,redirect
from manager.forms import TurfForm
from website.models import TurfManager
from manager.models import Turf

# Create your views here.

def index(request):
    return render(request,'manager/index.html')

def add_turf(request):
    add_turf = TurfForm()
    print(request.user,"#")
    manager_obj = TurfManager.objects.get(user=request.user)
    if request.method == 'POST':
        add_turf = TurfForm(request.POST)
        print(add_turf)
        if add_turf.is_valid():
            valdat = add_turf.save()
            Turf.objects.filter(id=valdat.id).update(manager=manager_obj)
            return redirect('manager:index')
    return render(request,'manager/add_turf.html')