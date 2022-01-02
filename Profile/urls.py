from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.doctors, name="doctors"),
    path('account/', views.account, name="account"),
    path('doctor/<str:pk>/', views.singleDoctor, name="doctor"),
    path('patient/<str:pk>/', views.singlePatient, name="patient"),
    path('doctor-signup/', views.signupDoctor, name="doctor-signup"),
    path('patient-signup/', views.signupPatient, name="patient-signup"),
    path('login/', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
    path('edit-profile/', views.editAccount, name="edit-profile"),
]