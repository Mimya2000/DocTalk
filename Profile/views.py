from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Patient, Doctor, CustomUser
from .forms import CustomUserCreationForm, DoctorCreationForm, PatientCreationForm, DoctorForm, PatientForm, DegreeForm
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from .utils import searchDoctors


def doctors(request):
    doctorObj, search_query = searchDoctors(request)
    context = {'doctors': doctorObj, 'search_query': search_query}
    return render(request, 'Profile/doctors.html', context)


@login_required(login_url='login')
def account(request):
    if request.user.is_doctor:
        doctorObj = request.user.doctor
        context = {'doctor': doctorObj}
        return render(request, 'Profile/doctor-account.html', context)
    else:
        patientObj = request.user.patient
        today = date.today()
        born = patientObj.dob
        if not born:
            age = 'unspecified'
        else:
            age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        context = {'patient': patientObj, 'age': age}
        return render(request, 'Profile/patient-account.html', context)


@login_required(login_url='login')
def editAccount(request):
    if request.user.is_doctor:
        doctorObj = request.user.doctor
        form = DoctorForm(instance=doctorObj)
        if request.method == 'POST':
            form = DoctorForm(request.POST, request.FILES, instance=doctorObj)
            if form.is_valid():
                form.save()
                return redirect('account')
    else:
        patientObj = request.user.patient
        form = PatientForm(instance=patientObj)
        if request.method == 'POST':
            form = PatientForm(request.POST, request.FILES, instance=patientObj)
            if form.is_valid():
                form.save()
                return redirect('account')
    context = {'form': form}
    return render(request, 'Profile/edit-profile.html', context)


@login_required(login_url='login')
def editDegree(request):
    doctor = request.user.doctor
    form = DegreeForm()
    if request.method == 'POST':
        form = DegreeForm(request.POST)
        if form.is_valid():
            degree = form.save(commit=False)
            degree.doc_id = doctor
            degree.save()
            messages.success(request, 'Degree was added successfully!')
            return redirect('account')
    context = {'form': form}
    return render(request, 'Profile/edit-degree.html', context)


def singleDoctor(request, pk):
    doctorObj = Doctor.objects.get(id=pk)
    if request.user.doctor == doctorObj:
        return redirect('account')
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
            login(request, doctor)
            return redirect('edit-profile')
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
                login(request, patient)
                return redirect('edit-profile')
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
            return redirect('account')
    return render(request, 'Profile/login.html')


def userLogout(request):
    logout(request)
    messages.info(request, 'You were logged out!')
    return redirect('login')


def passwordReset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['email']
            associated_users = CustomUser.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "Text/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        "name": user.name,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'DocTalk',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(
                            subject,
                            email,
                            settings.EMAIL_HOST_USER,
                            [user.email],
                            fail_silently=False,
                        )
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect("password_reset_done")
            messages.error(request, 'An invalid email has been entered.')
    form = PasswordResetForm()
    context = {'form': form}
    return render(request, 'reset_password.html', context)