from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.views.decorators.csrf import csrf_exempt

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
        else:
            messages.info(request, "Invalid Credentials")
    return render(request, "website/login.html")

def sign_up(request):
    return render(request,'website/signin.html')

def logout_view(request):
    logout(request)
    return redirect("website:login")

