from . import views
from django.urls import path

app_name = 'turfuser'

urlpatterns = [
    path('index',views.index,name="index"),
    path('about',views.about,name="about"),
    path('gallery',views.gallery,name="gallery"),
    path('logout',views.logout_view,name="logout"),
    path('turf-view/<int:id>',views.turf_view,name="turf_view"),
    path('book/<int:id>',views.book,name="book"),
    path('turfs',views.turfs,name="turfs"),
    path('contact',views.contact,name="contact"),
    path('search/',views.search, name='search'),
]