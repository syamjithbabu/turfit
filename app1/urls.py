from . import views
from django.urls import path

app_name = 'main_admin'

urlpatterns = [
    path('home',views.home,name="home"),
    path('sample',views.sample,name="sample"),
    path('add-manager',views.add_manager,name="add_manager"),
    path('view-manager',views.view_manager,name="view_manager")
]