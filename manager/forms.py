from manager.models import Turf

from django import forms
from django.forms.widgets import DateInput
from django.forms.widgets import EmailInput
from django.forms.widgets import NumberInput
from django.forms.widgets import Select
from django.forms.widgets import Textarea
from django.forms.widgets import TextInput
from django.forms.widgets import FileInput


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