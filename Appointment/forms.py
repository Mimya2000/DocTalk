from django.forms import ModelForm
from django import forms
from .models import Appointment


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['date']

