from django.shortcuts import render,redirect
from django.contrib.auth import login,logout

# Create your views here.

def index(request):
    return render(request,'turfuser/index.html')

def logout_view(request):
    logout(request)
    return redirect("website:login")