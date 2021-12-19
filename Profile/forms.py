from django.forms import ModelForm
from .models import Patient, Doctor

#
# class patient_signup_form(ModelForm):
#     class Meta:
#         model = Patient
#         fields = '__all__'


class doctor_signup_form(ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'email', 'phone', 'reg_num', 'password1', 'password2']

