from django.conf import settings
from django.contrib import messages
from datetime import datetime
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from Profile.models import Doctor, Patient
from .forms import AppointmentForm
from .models import Appointment
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def appointment(request, pk):
    form = AppointmentForm()
    doctor = Doctor.objects.get(id=pk)
    patient = request.user.patient
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            now = datetime.now()
            date = form.cleaned_data.get('date')
            if (now.year == date.year and now.month < date.month) or (now.year == date.year and now.month == date.month and now.day < date.day) or (now.year == date.year and now.month == date.month and now.day == date.day):
                appoint = form.save(commit=False)
                appoint.doc_id = doctor
                appoint.patient_id = patient
                appoint.save()
                subject = 'New Appointment!'
                email1 = 'Hey ' + str(doctor.name) + ', you have an appointment with ' + str(patient.name) + ' on ' + str(date.day) + '/' + str(date.month) + '/' + str(date.year) + '.'
                email2 = 'Hey ' + str(patient.name) + ', you have set an appointment with ' + str(doctor.name) + ' on ' + str(date.day) + '/' + str(date.month) + '/' + str(date.year) + '.'
                # send_mail(
                #     subject,
                #     email1,
                #     settings.EMAIL_HOST_USER,
                #     [doctor.email],
                #     fail_silently=False,
                # )
                send_mail(
                    subject,
                    email2,
                    settings.EMAIL_HOST_USER,
                    [patient.email],
                    fail_silently=False,
                )
                messages.success(request, 'Your Appointment Was Set Successfully!')
                return redirect('account')
        messages.error(request, 'Something Went Wrong. Please Try Again!')
    context = {'form': form, 'doctor': doctor, 'patient': patient}
    return render(request, 'Appointment/appointment.html', context)


@login_required(login_url='login')
def appointments(request):
    if request.user.is_doctor:
        doctor = request.user.doctor
        appoint = Appointment.objects.all().filter(doc_id=doctor)
    else:
        patient = request.user.patient
        appoint = Appointment.objects.all().filter(patient_id=patient)
    now = datetime.now().date()
    today = appoint.filter(date__year=now.year, date__month=now.month, date__day=now.day)
    future = appoint.filter(date__gt=now)
    past = appoint.filter(date__lt=now)
    context = {'today': today, 'future': future, 'past': past}
    return render(request, 'Appointment/my-appointments.html', context)
