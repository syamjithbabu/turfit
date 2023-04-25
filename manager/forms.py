from manager.models import Turf, Event

from django import forms
from django.forms.widgets import DateInput
from django.forms.widgets import EmailInput
from django.forms.widgets import NumberInput
from django.forms.widgets import Select
from django.forms.widgets import Textarea
from django.forms.widgets import TextInput
from django.forms.widgets import FileInput
from django.forms.widgets import TimeInput


class TurfForm(forms.ModelForm):
    class Meta:
        model = Turf
        fields = (
            "id",
            "turf_name",
            "turf_place",
            "phone",
            "turf_image"        
        )
        widgets = {
            "turf_name": TextInput(
                attrs={"class": "form-control", "name": "turf_name", "placeholder": "Name", "required": "required", "autocomplete": "off", "id": "editname"}
            ),
            "phone": TextInput(attrs={"class": "form-control", "name": "phone", "placeholder": "Phone", "required": "required", "autocomplete": "off"}),
            "address": TextInput(attrs={"class": "form-control", "name": "turf_place", "placeholder": "Address", "required": "required", "autocomplete": "off"}),
            "turf_image": FileInput(attrs={'class': 'form-control-file',"name": "turf_image",}),
            
}

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (
            "id",
            "event_title",
            "date",
            "time",
            "event_image" ,
            "entry_fee",
            "strength",
            "game",
            "turf"       
        )
        widgets = {
            "event_title": TextInput(
                attrs={"class": "form-control", "name": "event_title", "placeholder": "Event Title", "required": "required", "autocomplete": "off", "id": "editname"}
            ),
            "date": DateInput(attrs={"class": "form-control", "name": "date", "placeholder": "Date", "required": "required", "autocomplete": "off"}),
            "time": TimeInput(attrs={"class": "form-control", "name": "time", "placeholder": "Address", "required": "required", "autocomplete": "off"}),
            "event_image": FileInput(attrs={'class': 'form-control-file',"name": "event_image",}),
            "entry_fee": TextInput(attrs={"class": "form-control", "name": "entry_fee", "placeholder": "Entry Fee", "required": "required", "autocomplete": "off"}),
            "strength": TextInput(attrs={"class": "form-control", "name": "strength", "placeholder": "Strength", "required": "required", "autocomplete": "off"}),
            "game": TextInput(attrs={"class": "form-control", "name": "game", "placeholder": "Game", "required": "required", "autocomplete": "off"}),
            "turf": TextInput(attrs={"class": "form-control", "name": "turf", "placeholder": "Turf", "required": "required", "autocomplete": "off"}),
}