from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'website/login.html')

def sign_up(request):
    return render(request,'website/signin.html')