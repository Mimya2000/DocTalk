from django.contrib import messages
from datetime import datetime
from django.shortcuts import render, redirect
from Profile.models import Doctor
from .forms import AppointmentForm


def appointment(request, pk):
    form = AppointmentForm()
    doctor = Doctor.objects.get(id=pk)
    patient = request.user.patient
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            now = datetime.now()
            date = form.cleaned_data.get('date')
            if (now.year == date.year and now.month < date.month) or (now.year == date.year and now.month == date.month and now.day < date.day):
                appoint = form.save(commit=False)
                appoint.doc_id = doctor
                appoint.patient_id = patient
                appoint.save()
                messages.success(request, 'Your Appointment Was Set Successfully!')
                return redirect('account')
        messages.error(request, 'Something Went Wrong. Please Try Again!')
    context = {'form': form, 'doctor': doctor, 'patient': patient}
    return render(request, 'Appointment/appointment.html', context)
