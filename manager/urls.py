from . import views
from django.urls import path

app_name = 'manager'

urlpatterns = [
    path('',views.index,name="index"),
    path('add-turf',views.add_turf,name="add_turf"),
    path('view-turf',views.view_turf,name="view_turf"),
    path('add-time-slot/<int:id>',views.add_time_slots,name="add_time_slots"),
    path('turf-delete/<int:id>',views.delete_turf,name="turf_delete"),
    path('turf-details/<int:id>',views.turf_details,name="turf_details"),
    path('slot-delete/<int:id>',views.delete_slot,name="delete_slot"),
    path('bookings',views.bookings,name="bookings"),
    path('reject-booking/<int:id>',views.reject_booking,name="reject_booking"),
    path('edit-time-slot/<int:id>',views.edit_time_slot,name="edit_time_slots"),
    path('add-agmes/<int:id>',views.add_games,name="add_games"),
    path('delete-game/<int:id>',views.delete_game,name="delete_game"),
    path('add-event',views.add_event,name="add_event"),
    path('view-event',views.view_events,name="view_events"),
    path('edit-event/<int:id>',views.edit_event,name="edit_event"),
    path('view-event-details/<int:id>',views.view_event_details,name="view_event_details"),
    path('delete-event/<int:id>',views.event_delete,name="event_delete"),
    path('booked-events',views.event_booking,name="booked_events"),
    path('delete-booked-event/<int:id>',views.booked_event_delete,name="delete_booked_event")
 
]