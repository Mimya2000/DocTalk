import uuid

from django.db import models

# Create your models here.
from Profile.models import Doctor, Patient


class Appointment(models.Model):
    doc_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.id)
