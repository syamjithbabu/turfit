from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from manager.models import Turf,TimeSlot,Category
from website.models import TurfUser
from django.db.models import Q

# Create your views here.

def index(request):
    turfs = Turf.objects.filter().all()
    context = {
        'turfs' : turfs
    }
    return render(request,'turfuser/index.html',context)

def about(request):
    return render(request,'turfuser/about-us.html')

def gallery(request):
    return render(request,'turfuser/gallery.html')

def turfs(request):
    turfs = Turf.objects.filter().all()
    context = {
        'turfs' : turfs
    }
    return render(request,'turfuser/turfs.html',context)

def contact(request):
    return render(request,'turfuser/contact.html')

def logout_view(request):
    logout(request)
    return redirect("website:login")

def turf_view(request,id):
    turf = Turf.objects.get(id=id)
    slots = TimeSlot.objects.filter(turf=turf)
    games = Category.objects.filter(turf=turf).all()
    context = {
        'turf' : turf,
        'slot' : slots,
        'games' : games
    }
    return render(request,'turfuser/turf_view.html',context)

def book(request,id):
    slot = TimeSlot.objects.get(id=id)
    turf_user = TurfUser.objects.get(user=request.user)
    print(turf_user)
    book_slot = TimeSlot.objects.filter(id=id).update(status = 1,turf_user=turf_user)
    print(book_slot)
    context = {
        'slot' : slot,
    }
    return render(request,'turfuser/book.html',context)

def search(request):
    if request.method == "POST":
        search = request.POST.get("q")
        results = Turf.objects.filter(turf_place__icontains=search)
        context = {"turfs": results,"query":search}
    return render(request, 'turfuser/search-results.html', context)