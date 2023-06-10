from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django import forms
from .models import CustomUser, Doctor, Patient, Degree


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'phone', 'password1', 'password2']
        labels = {
            'name': 'Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class DoctorCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'phone', 'reg_num', 'password1', 'password2']
        labels = {
            'name': 'Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'reg_num': 'Registration Number',
        }

        def __init__(self, *args, **kwargs):
            super(DoctorCreationForm, self).__init__(*args, **kwargs)
            self.fields['name'].widget.attrs.update(
                {'class': 'form-control', 'id': 'name', 'placeholder': 'Enter your name', 'style': 'color: #2F4F4F;'})
            self.fields['email'].widget.attrs.update(
                {'class': 'form-control', 'id': 'email', 'placeholder': 'Enter your Email Address',
                 'style': 'color: #2F4F4F;'})
            self.fields['phone'].widget.attrs.update(
                {'class': 'form-control', 'id': 'phone', 'placeholder': 'Enter your Phone Number',
                 'style': 'color: #2F4F4F;'})
            self.fields['reg_num'].widget.attrs.update(
                {'class': 'form-control', 'id': 'reg_num', 'placeholder': 'Enter your Registration Number',
                 'style': 'color: #2F4F4F;'})
            self.fields['password1'].widget.attrs.update(
                {'class': 'form-control', 'id': 'password', 'placeholder': 'Enter your Password',
                 'style': 'color: #2F4F4F;'})
            self.fields['password2'].widget.attrs.update(
                {'class': 'form-control', 'id': 'password2', 'placeholder': 'Confirm your Password',
                 'style': 'color: #2F4F4F;'})


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'email', 'phone', 'c_address', 'reg_num', 'bkash_no', 'specialization',
                  'fees_new', 'fees_old', 'fees_report', 'doc_image']


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'email', 'phone', 'gender', 'dob', 'feet', 'inch', 'weight', 'asthma',
                  'is_diabetic', 'bs_before', 'bs_after', 'allergic', 'systole', 'diastole', 'patient_image']
        widgets = {
            'allergic': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['allergic'].widget.attrs.update({'class': 'larger'})


class PatientCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'phone', 'password1', 'password2']
        labels = {
            'name': 'Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
        }

    def __init__(self, *args, **kwargs):
        super(PatientCreationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'id': 'name', 'placeholder': 'Enter your name', 'style': 'color: #2F4F4F;'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'id': 'email', 'placeholder': 'Enter your Email Address', 'style': 'color: #2F4F4F;'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'id': 'phone', 'placeholder': 'Enter your Phone Number', 'style': 'color: #2F4F4F;'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'id': 'password', 'placeholder': 'Enter your Password', 'style': 'color: #2F4F4F;'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'id': 'password2', 'placeholder': 'Confirm your Password', 'style': 'color: #2F4F4F;'})
        # for name, field in self.fields.items():
        #     if field.error_messages:
        #         field.widget.attrs.update({'class': 'form-control error'})
        #     else:
        #         field.widget.attrs.update({'class': 'form-control success'})


class DegreeForm(ModelForm):
    class Meta:
        model = Degree
        fields = '__all__'
        exclude = ['doc_id']

