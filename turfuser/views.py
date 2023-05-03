from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from manager.models import Turf,TimeSlot,Category,Event,EventBook
from website.models import TurfUser
from turfuser.models import Contact
from django.db.models import Q

# Create your views here.

def index(request):
    turfs = Turf.objects.filter().all()
    events = Event.objects.filter().all()
    context = {
        'turfs' : turfs,
        'events' : events
    }
    return render(request,'turfuser/index.html',context)

def about(request):
    return render(request,'turfuser/about-us.html')

def events(request):
    events = Event.objects.filter().all()
    context = {
        'events' : events
    }
    return render(request,'turfuser/gallery.html',context)

def turfs(request):
    turfs = Turf.objects.filter().all()
    context = {
        'turfs' : turfs
    }
    return render(request,'turfuser/turfs.html',context)

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('contact-first-name')
        second_name = request.POST.get('contact-last-name')
        email = request.POST.get('contact-email')
        phone = request.POST.get('contact-phone')
        message = request.POST.get('contact-message')
        contact = Contact.objects.create(first_name=first_name,second_name=second_name,email=email,phone=phone,message=message)
        contact.save()
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

def event_details(request,id):
    events_book = Event.objects.get(id=id)
    turf_user = TurfUser.objects.get(user=request.user)
    booked = EventBook.objects.filter(user=turf_user,event=id)
    context = {
        'event' : events_book,
        'booked' : booked
    }
    return render(request,'turfuser/event_booking.html',context)

def event_booking(request,id):
    print("Working")
    events_book = Event.objects.get(id=id)
    turf_user = TurfUser.objects.get(user=request.user)
    print(turf_user)
    if EventBook.objects.filter(user=turf_user,event=id):
        print("Already Registered")
    else:
        EventBook.objects.filter(id=id).create(event=events_book,user=turf_user,manager=events_book.manager)
    return redirect('turfuser:events')

def orders(request):
    user_obj = TurfUser.objects.get(user=request.user)
    event_booking = EventBook.objects.filter(user=user_obj).all()
    context = {
        'events' : event_booking,
    }
    return render(request,'turfuser/orders.html',context)

def remove_event(request,id):
    remove = EventBook.objects.get(id=id)
    remove.delete()
    return redirect('turfuser:orders')

def turf_orders(request):
    user_obj = TurfUser.objects.get(user=request.user)
    turf_orders = TimeSlot.objects.filter(turf_user=user_obj,status=1).all()
    context = {
        'orders' : turf_orders
    }
    return render(request,'turfuser/turf-bookings.html',context)

def remove_turf(request,id):
    turf = TimeSlot.objects.get(id=id)
    user_obj = TurfUser.objects.get(user=request.user)
    remove_turf = TimeSlot.objects.filter(turf_user=user_obj,turf=turf.turf).update(status=0)
    return redirect('turfuser:turf_orders')