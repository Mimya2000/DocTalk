from django.urls import path
from . import views

urlpatterns = [
    path('appointment/<str:pk>/', views.appointment, name="appointment"),
    path('my/appointments/', views.appointments, name="my-appointments"),
]
