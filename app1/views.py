from django.shortcuts import render, redirect
from website.forms import LoginForm
from website.forms import UserRegistration
from website.models import User,TurfManager
from manager.models import Turf,TimeSlot,EventBook
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from turfuser.models import Contact

# Create your views here.

def home(request):
    bookings = TimeSlot.objects.filter(status=1).all()
    all_turfs = Turf.objects.filter().count()
    all_managers = TurfManager.objects.filter().count()
    all_enquiries = Contact.objects.filter().count()
    context = {
        'bookings' : bookings,
        'all_turfs' : all_turfs,
        'all_managers' : all_managers,
        'all_enquiries' : all_enquiries
    }
    return render(request,'app1/index.html',context)

def sample(request):
    return render(request,'app1/sample.html')

@csrf_exempt
def add_manager(request):
    login_form = LoginForm()
    user_form = UserRegistration()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        user_form = UserRegistration(request.POST)
        user_email = user_form["email"].value()
        if login_form.is_valid() and user_form.is_valid():
            user = login_form.save(commit=False)
            user.is_turfmanager = True
            user.save()
            c = user_form.save(commit=False)
            c.user = user
            c.save()
            User.objects.filter(id=user.id).update(email=user_email)
            messages.info(request, "Manager Registration Successfully")
            return redirect("main_admin:home")
    return render(request,'app1/add_manager.html',{"login_form": login_form, "user_form": user_form})

def view_manager(request):
    managers = TurfManager.objects.filter().all()
    context = {
        'managers' : managers
    }
    return render(request,'app1/view_turf_manager.html',context)

def view_turf(request):
    turfs = Turf.objects.filter().all()
    context ={
        'turfs':turfs
    }
    return render(request,'app1/view_turf.html',context)

def delete_manager(request,id):
    manager = TurfManager.objects.get(id=id)
    manager.delete()
    return redirect('main_admin:view_manager')

def bookings(request):
    bookings = TimeSlot.objects.filter(status=1)
    context = {
        'bookings' : bookings
    }
    return render(request,'app1/bookings.html',context)

def enquiries(request):
    enquiries = Contact.objects.filter().all()
    context = {
        'enquiries' : enquiries
    }
    return render(request,'app1/enquiries.html',context)

def reply(request,id):
    user = Contact.objects.get(id=id)
    context = {
        'user' : user
    }
    if request.method == 'POST':
        reply = request.POST.get('reply')
        print(reply)
        enquiry_reply = Contact.objects.filter(id=id).update(reply=reply)
        return redirect('main_admin:enquiries')
    return render(request,'app1/reply.html',context)

def event_bookings(request):
    event_bookings = EventBook.objects.filter().all()
    context = {
        'bookings' : event_bookings
    }
    return render(request,'app1/event_bookings.html',context)

def remove_enquiry(request,id):

    return redirect('main_admin:enquiries')

