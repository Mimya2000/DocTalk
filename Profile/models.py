from django.db import models
from django.contrib.auth.models import User, AbstractUser
import uuid


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    c_address = models.TextField(max_length=1024)
    reg_num = models.CharField(max_length=10)
    bkash_no = models.CharField(max_length=11)
    specializations = models.ManyToManyField('Specialization')
    # degrees = models.ManyToManyField('Degree')
    fees_new = models.IntegerField()
    fees_old = models.IntegerField()
    fees_report = models.IntegerField()
    doc_image = models.ImageField(null=True, blank=True, upload_to='doctors/', default="doctors/doctor-default.jpg")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.email


class Degree(models.Model):
    name = models.CharField(max_length=200)
    institute = models.CharField(max_length=500)
    doc_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.doc_id


class Specialization(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


########################################## PATIENT ######################################

class Patient(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    feet = models.CharField(max_length=5, null=True, blank=True)
    inch = models.CharField(max_length=5, null=True, blank=True)
    weight = models.CharField(max_length=5, null=True, blank=True)
    dob = models.DateTimeField()
    asthma = models.BooleanField()
    is_diabetic = models.BooleanField(default=False)
    bs_before = models.CharField(max_length=5, null=True, blank=True)
    bs_after = models.CharField(max_length=5, null=True, blank=True)
    allergic = models.ManyToManyField('Allergies', blank=True)
    systole = models.CharField(max_length=5, null=True, blank=True)
    diastole = models.CharField(max_length=5, null=True, blank=True)
    patient_image = models.ImageField(null=True, blank=True, upload_to='patients/',
                                      default="patients/patient-default.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.email


class Allergies(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

