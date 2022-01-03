from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
import uuid


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11, unique=True)
    reg_num = models.CharField(max_length=10, blank=True, null=True)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = False


########################################## DOCTOR ######################################


class Doctor(models.Model):
    SPECIALIZATION = (
        ('Internal medicine', 'Internal medicine'),
        ('Pediatricians', 'Pediatricians'),
        ('Geriatric medicine', 'Geriatric medicine'),
        ('Allergists', 'Allergists'),
        ('Dermatologists', 'Dermatologists'),
        ('Anesthesiologists', 'Anesthesiologists'),
        ('Cardiac surgeons', 'Cardiac surgeons'),
        ('Ophthalmologists', 'Ophthalmologists'),
        ('Orthopedic surgeons', 'Orthopedic surgeons'),
        ('Obstetrician/gynecologists', 'Obstetrician/gynecologists'),
        ('General surgeons', 'General surgeons'),
        ('Cardiologists', 'Cardiologists'),
        ('Endocrinologists', 'Endocrinologists'),
        ('Rheumatologists', 'Rheumatologists'),
        ('Radiologists', 'Radiologists'),
        ('Gastroenterologists', 'Gastroenterologists'),
        ('Oncologists', 'Oncologists'),
        ('Nephrologists', 'Nephrologists'),
        ('Urologists', 'Urologists'),
        ('Pulmonologists', 'Pulmonologists'),
        ('Psychiatrists', 'Psychiatrists'),
        ('Otolaryngologists', 'Otolaryngologists'),
        ('Neurologists', 'Neurologists'),
    )
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11, unique=True)
    c_address = models.TextField(max_length=1024, blank=True, null=True)
    reg_num = models.CharField(max_length=10, blank=True, null=True)
    bkash_no = models.CharField(max_length=11, blank=True, null=True)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION, default='Internal medicine')
    fees_new = models.IntegerField(blank=True, null=True)
    fees_old = models.IntegerField(blank=True, null=True)
    fees_report = models.IntegerField(blank=True, null=True)
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



########################################## PATIENT ######################################



class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11, unique=True)
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER_CHOICES)
    feet = models.CharField(max_length=5, null=True, blank=True)
    inch = models.CharField(max_length=5, null=True, blank=True)
    weight = models.CharField(max_length=5, null=True, blank=True)
    dob = models.DateField(blank=True, null=True)
    asthma = models.BooleanField(blank=True, null=True)
    is_diabetic = models.BooleanField(default=False, blank=True, null=True)
    bs_before = models.CharField(max_length=5, null=True, blank=True)
    bs_after = models.CharField(max_length=5, null=True, blank=True)
    allergic = models.ManyToManyField('Allergies', blank=True)
    systole = models.CharField(max_length=5, null=True, blank=True)
    diastole = models.CharField(max_length=5, null=True, blank=True)
    patient_image = models.ImageField(null=True, blank=True, upload_to='patients/', default="patients/patient-default.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.email


class Allergies(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
