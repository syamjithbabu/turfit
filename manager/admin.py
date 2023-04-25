from django.contrib import admin
from manager.models import Turf,TimeSlot,Event,EventBook

# Register your models here.

admin.site.register(Turf)
admin.site.register(TimeSlot)
admin.site.register(Event)
admin.site.register(EventBook)
