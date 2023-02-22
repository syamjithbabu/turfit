import re

from .models import TurfManager
from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.widgets import EmailInput
from django.forms.widgets import TextInput


class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


def phone_number_validation(value):
    if not re.compile(r"[0-9]\d{9}$").match(value):
        raise ValidationError("This is Not Valid Phone Number")


class UserRegistration(forms.ModelForm):
    phone = forms.CharField(
        validators=[phone_number_validation],
        widget=TextInput(attrs={"class": "form-control", "name": "phone", "placeholder": "phone", "required": "required", "autocomplete": "off"}),
    )

    class Meta:
        model = TurfManager
        fields = ("name", "email", "phone", "turf_place", "district")
        widgets = {
            "name": TextInput(attrs={"class": "form-control", "name": "name", "placeholder": "Name", "required": "required", "autocomplete": "off"}),
            "email": EmailInput(attrs={"class": "form-control", "name": "email", "placeholder": "Email", "required": "required", "autocomplete": "off"}),
            "turf_place": TextInput(
                attrs={"class": "form-control", "name": "turfplace", "placeholder": "Turf Place", "required": "required", "autocomplete": "off"}
            ),
            "district": TextInput(attrs={"class": "form-control", "name": "district", "placeholder": "District", "required": "required", "autocomplete": "off"}),
        }