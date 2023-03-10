from django.shortcuts import render,redirect
from manager.forms import TurfForm
from website.models import TurfManager
from manager.models import Turf,TimeSlot

# Create your views here.

def index(request):
    return render(request,'manager/index.html')

def add_turf(request):
    add_turf = TurfForm()
    print(request.user,"#")
    manager_obj = TurfManager.objects.get(user=request.user)
    if request.method == 'POST':
        add_turf = TurfForm(request.POST, request.FILES)
        print(add_turf)
        if add_turf.is_valid():
            valdat = add_turf.save()
            Turf.objects.filter(id=valdat.id).update(manager=manager_obj)
            return redirect('manager:view_turf')
    return render(request,'manager/add_turf.html')

def view_turf(request):
    manager_obj = TurfManager.objects.get(user=request.user)
    print(manager_obj,"#")
    turfs = Turf.objects.filter(manager=manager_obj)
    context = {
        'turfs' : turfs
    }
    return render(request,'manager/view_turfs.html',context)

def add_time_slots(request,id):
    turf = Turf.objects.get(id=id)
    print(turf.turf_name)
    if request.method == 'POST':
        start_time = request.POST.get('starttime')
        end_time = request.POST.get('endtime')
        time_slot = TimeSlot.objects.create(turf=turf,start_time=start_time,end_time=end_time)
        time_slot.save()
        return redirect('manager:view_turf')
    return render(request,'manager/add_time_slot.html')

def delete_turf(request,id):
    turf = Turf.objects.get(id=id)
    turf.delete()
    return redirect('manager:index')

def turf_details(request,id):
    turf = Turf.objects.get(id=id)
    time_slots = TimeSlot.objects.filter(turf=turf)
    context = {
        'turf': turf,
        'slot' : time_slots
    }
    return render(request,'manager/turf_details.html',context)