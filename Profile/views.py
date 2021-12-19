from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Patient, Doctor
from .forms import doctor_signup_form


def doctors(request):
    doctorObj = Doctor.objects.all()
    context = {'doctors': doctorObj}
    return render(request, 'Profile/doctors.html', context)


def singleDoctor(request, pk):
    # doctorObj = Doctor.objects.get(id=pk)
    # context = {'doctor': doctorObj}
    return render(request, 'Profile/doctor-profile.html')


def singlePatient(request, pk):
    # patientObj = Patient.objects.get(id=pk)
    # context = {'patient': patientObj}
    return render(request, 'Profile/patient-profile.html')


def registerDoctor(request):
    form = doctor_signup_form()
    if request.method == 'POST':
        form = doctor_signup_form(request.POST)
        if form.is_valid():
            messages.success(request, 'User account was created!')
            return redirect('profiles')
        else:
            messages.error(request, 'An error has occurred during registration.')
    context = {'form': form}
    return render(request, 'Profile/doctor-signup.html', context)
