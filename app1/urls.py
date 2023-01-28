from . import views
from django.urls import path

app_name = 'app1'

urlpatterns = [
    path('home',views.home,name="home"),
    path('sample',views.sample,name="sample")
]