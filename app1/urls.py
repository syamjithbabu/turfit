from . import views
from django.urls import path

app_name = 'main_admin'

urlpatterns = [
    path('home',views.home,name="home"),
    path('sample',views.sample,name="sample"),
    path('add-manager',views.add_manager,name="add_manager"),
    path('view-manager',views.view_manager,name="view_manager"),
    path('view-turf',views.view_turf,name="view_turf"),
    path('delete-manager/<int:id>',views.delete_manager,name="delete_manager"),
    path('bookings',views.bookings,name="bookings"),
    path('enquiries',views.enquiries,name="enquiries"),
    path('reply/<int:id>',views.reply,name="reply"),
    path('event-bookings',views.event_bookings,name="event_bookings"),
    path('remove-enquiry/<int:id>',views.remove_enquiry,name="remove_enquiry")
]