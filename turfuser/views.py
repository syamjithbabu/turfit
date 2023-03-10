from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from manager.models import Turf,TimeSlot

# Create your views here.

def index(request):
    turfs = Turf.objects.filter().all()
    context = {
        'turfs' : turfs
    }
    return render(request,'turfuser/index.html',context)

def logout_view(request):
    logout(request)
    return redirect("website:login")

def turf_view(request,id):
    turf = Turf.objects.get(id=id)
    slots = TimeSlot.objects.filter(turf=turf)
    context = {
        'turf' : turf,
        'slot' : slots
    }
    return render(request,'turfuser/turf_view.html',context)