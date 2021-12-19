from django.urls import path
from . import views


urlpatterns = [
    path('', views.doctors, name="doctors"),
    path('doctor/<str:pk>/', views.singleDoctor, name="doctor"),
    path('patient/<str:pk>/', views.singlePatient, name="patient"),
    path('doctor-signup', views.registerDoctor, name="doctor-signup"),
]