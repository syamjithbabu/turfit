from . import views
from django.urls import path

app_name = 'manager'

urlpatterns = [
    path('',views.index,name="index"),
    path('add-turf',views.add_turf,name="add_turf")
]