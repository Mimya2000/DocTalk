from django.contrib import admin
from .models import Doctor, Degree, Specialization, Patient, Allergies

admin.site.register(Doctor)
admin.site.register(Degree)
admin.site.register(Specialization)
admin.site.register(Patient)
admin.site.register(Allergies)


