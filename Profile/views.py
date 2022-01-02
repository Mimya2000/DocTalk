from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Patient, Doctor, CustomUser
from .forms import CustomUserCreationForm, DoctorCreationForm, PatientCreationForm
from datetime import date
from django.contrib.auth.decorators import login_required


def doctors(request):
    doctorObj = Doctor.objects.all()
    context = {'doctors': doctorObj}
    return render(request, 'Profile/doctors.html', context)


@login_required(login_url='login')
def account(request):
    if request.user.is_doctor:
        doctorObj = request.user.doctor
        context = {'doctor': doctorObj}
        return render(request, 'Profile/doctor-profile.html', context)
    else:
        patientObj = request.user.patient
        today = date.today()
        born = patientObj.dob
        if not born:
            age = 'unspecified'
        else:
            age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        context = {'patient': patientObj, 'age': age}
        return render(request, 'Profile/patient-profile.html', context)


def singleDoctor(request, pk):
    doctorObj = Doctor.objects.get(id=pk)
    context = {'doctor': doctorObj}
    return render(request, 'Profile/doctor-profile.html', context)


def singlePatient(request, pk):
    patientObj = Patient.objects.get(id=pk)
    today = date.today()
    born = patientObj.dob
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    context = {'patient': patientObj, 'age': age}
    return render(request, 'Profile/patient-profile.html', context)


def signupDoctor(request):
    form = DoctorCreationForm()
    if request.method == 'POST':
        form = DoctorCreationForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.is_doctor = True
            doctor.save()
            messages.success(request, 'Account was created!')
            return redirect('doctors')
            # return redirect(reverse('doctor-register', kwargs={"user": user}))
            # return redirect('doctor-register', user=user)
        else:
            messages.error(request, 'An error has occurred during registration.')
    context = {'form': form}
    return render(request, 'Profile/doctor-signup.html', context)


def signupPatient(request):
    form = PatientCreationForm()
    # for field in form.errors:
    #     form[field].field.widget.attrsupdate({'class': 'form-control.error input'})
    # for field in form.success:
    #     form[field].field.widget.attrsupdate({'class': 'form-control.success input'})
    if request.method == 'POST':
        form = PatientCreationForm(request.POST)
        num = request.POST['phone']
        if form.is_valid():
            if len(str(num)) == 11 and str(num).isnumeric:
                patient = form.save(commit=False)
                patient.is_patient = True
                patient.save()
                messages.success(request, 'Account was created!')
                return redirect('doctors')
            else:
                messages.error(request, 'Enter valid phone number.')
        else:
            messages.error(request, 'An error has occurred during registration.')
    context = {'form': form}
    return render(request, 'Profile/patient-signup.html', context)


def userLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        try:
            user = CustomUser.objects.get(email=email)
        except:
            messages.error(request, 'Email does not exist!')
            return render(request, 'Profile/login.html')
        user = authenticate(request, email=email, password=password)
        if user is None:
            messages.error(request, "Email or Password is incorrect!")
        else:
            login(request, user)
            return redirect('doctors')
    return render(request, 'Profile/login.html')


def userLogout(request):
    logout(request)
    messages.info(request, 'You were logged out!')
    return redirect('login')


