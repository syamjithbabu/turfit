from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm
from .forms import UserRegistration,SignRegistration

# Create your views here.

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pass")

        if not username or not password:
            messages.success(request, "Both Username and Password Required")
            return redirect("/")

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, "User not found")
            return redirect("/")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.success(request, "Wrong Paasword")
            return redirect("/")

        if user:
            login(request, user)

            if user.is_staff:
                return redirect("main_admin:home")
            elif user.is_turfmanager:
                return redirect("manager:index")
            elif user.is_user:
                return redirect("turfuser:index")
        else:
            messages.info(request, "Invalid Credentials")
    return render(request, "website/login.html")

def sign_up(request):
    login_form = LoginForm()
    user_form = SignRegistration()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        user_form = SignRegistration(request.POST)
        print(login_form)
        print(user_form)
        if login_form.is_valid() and user_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()
            c = user_form.save(commit=False)
            c.user = user
            c.save()
            messages.info(request, "User Registration Successfully")
            return redirect("website:login")
    return render(request,'website/signin.html',{"login_form": login_form, "user_form": user_form})

def logout_view(request):
    logout(request)
    return redirect("website:login")

