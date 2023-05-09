from django.shortcuts import render,redirect
from manager.forms import TurfForm,EventForm
from website.models import TurfManager
from manager.models import Turf,TimeSlot,Category,Event,EventBook
from turfuser.models import BookDate

# Create your views here.

def index(request):
    manager_obj = TurfManager.objects.get(user=request.user)
    bookings = TimeSlot.objects.filter(manager=manager_obj,status=1).all()
    booked_events = EventBook.objects.filter(manager=manager_obj).count()
    booked_turfs = TimeSlot.objects.filter(manager=manager_obj,status=1).count()
    print(manager_obj)
    print(bookings)
    context = {
        'bookings' : bookings,
        'events_count' : booked_events,
        'turfs_count' : booked_turfs
    }
    return render(request,'manager/index.html',context)

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
    return render(request,'manager/add_turf.html',)

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
    manager_obj = TurfManager.objects.get(user=request.user)
    if request.method == 'POST':
        start_time = request.POST.get('starttime')
        end_time = request.POST.get('endtime')
        price = request.POST.get('rate')
        avail_date = request.POST.get('date')
        print(avail_date)
        time_slot = TimeSlot.objects.create(turf=turf,start_time=start_time,end_time=end_time,price=price,manager=manager_obj,date_for_book=avail_date)
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
    games = Category.objects.filter(turf=turf)
    context = {
        'turf': turf,
        'slot' : time_slots,
        'games' : games,
    }
    for i in time_slots:
        if i.is_booked == True:
            i.status = 1
        else:
            i.status = 2
    if request.method == 'POST':
        turf_name = request.POST.get('turf_name')
        phone = request.POST.get('phone')
        address = request.POST.get('place')
        edit_turf = Turf.objects.filter(id=id).update(turf_name=turf_name,phone=phone,turf_place=address)
        return redirect('manager:view_turf')
    return render(request,'manager/turf_details.html',context)

def delete_slot(request,id):
    slot = TimeSlot.objects.get(id=id)
    print(slot)
    slot.delete()
    return redirect('manager:view_turf')

def bookings(request):
    manager_obj = TurfManager.objects.get(user=request.user)
    bookings = TimeSlot.objects.filter(manager=manager_obj,status=1)
    context = {
        'bookings' : bookings
    }
    return render(request,'manager/bookings.html',context)

def reject_booking(request,id):
    reject_book = TimeSlot.objects.filter(id=id).update(status=0)
    return render(request,'manager/bookings.html')

def edit_time_slot(request,id):
    edit_rate = TimeSlot.objects.get(id=id)
    print(edit_rate.id)
    print(edit_rate.start_time)
    context = {
        'rate' : edit_rate
    }
    if request.method == 'POST':
        start_time = request.POST.get('starttime')
        end_time = request.POST.get('endtime')
        price = request.POST.get('rate')
        time_slot = TimeSlot.objects.filter(id=id).update(start_time=start_time,end_time=end_time,price=price)
        return redirect('manager:view_turf')
    return render(request,'manager/edit_time_slots.html',context)

def add_games(request,id):
    turf = Turf.objects.get(id=id)
    if request.method == 'POST':
        game = request.POST.get('game')
        date = request.POST.get('date')
        BookDate.objects.create(date=date)
        game_category = Category.objects.create(turf=turf,game=game)
        return redirect('manager:view_turf')
    return render(request,'manager/add_games.html')

def delete_game(request,id):
    game = Category.objects.get(id=id)
    game.delete()
    return redirect('manager:view_turf')

def add_event(request):
    manager_obj = TurfManager.objects.get(user=request.user)
    print(manager_obj)
    turfs = Turf.objects.filter(manager=manager_obj).all()
    context = {
        'turfs' : turfs
    }
    if request.method == 'POST':
        add_event = EventForm(request.POST, request.FILES)
        print(add_event)
        if add_event.is_valid():
            valdat = add_event.save()
            Event.objects.filter(id=valdat.id).update(manager=manager_obj)
            return redirect('manager:view_events')
    return render(request,'manager/add_event.html',context)

def view_events(request):
    manager_obj = TurfManager.objects.get(user=request.user)
    events = Event.objects.filter(manager = manager_obj).all()
    context = {
        'events' : events
    }
    return render(request,'manager/view_events.html',context)

def edit_event(request,id):
    manager_obj = TurfManager.objects.get(user=request.user)
    edit_event = Event.objects.get(id=id)
    turfs = Turf.objects.filter(manager=manager_obj).all()
    context = {
        'event' : edit_event,
        'turfs' : turfs
    }
    if request.method == 'POST':
        add_event = EventForm(request.POST, request.FILES)
        print(add_event)
        event_title = request.POST.get('event_title')
        date = request.POST.get('date')
        time = request.POST.get('time')
        entry_fee = request.POST.get('entry_fee')
        strength = request.POST.get('strength')
        game = request.POST.get('game')
        if add_event.is_valid():
            print(id)
            Event.objects.filter(id=id).update(manager=manager_obj,turf=edit_event.turf,event_title=event_title,date=date,time=time,entry_fee=entry_fee,strength=strength,game=game)
            return redirect('manager:view_events')
    return render(request,'manager/edit_events.html',context)

def view_event_details(request,id):
    event = Event.objects.get(id=id)
    context = {
        'event' : event
    }
    return render(request,'manager/view_event_details.html',context)

def event_delete(request,id):
    delete_event = Event.objects.get(id=id)
    delete_event.delete()
    return render(request,'manager/view_events.html')

def event_booking(request):
    manager_object = TurfManager.objects.get(user=request.user)
    event_bookings = EventBook.objects.filter(manager=manager_object).all()
    context = {
        'bookings' : event_bookings
    }
    return render(request,'manager/event_bookings.html',context)

def booked_event_delete(request,id):
    delete_booking = EventBook.objects.get(id=id)
    delete_booking.delete()
    return render(request,'manager/index.html')