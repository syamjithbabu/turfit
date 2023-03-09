from . import views
from django.urls import path

app_name = 'turfuser'

urlpatterns = [
    path('index',views.index,name="index"),
    path('logout',views.logout_view,name="logout")
]