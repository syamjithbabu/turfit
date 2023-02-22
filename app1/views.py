from django.shortcuts import render, redirect
from website.forms import LoginForm
from website.forms import UserRegistration
from website.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request,'admin/index.html')

def sample(request):
    return render(request,'admin/sample.html')

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
    return render(request,'admin/add_manager.html',{"login_form": login_form, "user_form": user_form})

def view_manager(request):
    return render(request,'admin/view_turf_manager.html')