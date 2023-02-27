from . import views
from django.urls import path

app_name = 'main_admin'

urlpatterns = [
    path('home',views.home,name="home"),
    path('sample',views.sample,name="sample"),
    path('add-manager',views.add_manager,name="add_manager"),
    path('view-manager',views.view_manager,name="view_manager"),
    path('add-turf',views.add_turf,name="add_turf"),
    path('view-turf',views.view_turf,name="view_turf")
]