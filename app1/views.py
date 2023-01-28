from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'admin/index.html')

def sample(request):
    return render(request,'admin/sample.html')