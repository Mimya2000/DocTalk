from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Doctor, Patient
from django.conf import settings
from django.core.mail import send_mail


@receiver(post_save, sender=get_user_model())
def ProfileCreated(sender, instance, created, **kwargs):
    if created:
        user = instance
        if user.is_doctor:
            profile = Doctor.objects.create(
                user=user,
                email=user.email,
                name=user.name,
                phone=user.phone,
                reg_num=user.reg_num,
            )
        else:
            profile = Patient.objects.create(
                user=user,
                email=user.email,
                name=user.name,
                phone=user.phone,
            )
            subject = 'Welcome to DocTalk'
            message = 'Hello ' + profile.name + '! We are glad that you are here!'
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [profile.email],
                fail_silently=False,
            )


@receiver(post_save, sender=Doctor)
def updateDoctor(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.name = profile.name
        user.email = profile.email
        user.phone = profile.phone
        user.reg_num = profile.reg_num
        user.save()
        subject = 'Profile Information Updated'
        message = 'Hello ' + profile.name + '! Your profile information has been updated!'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


@receiver(post_save, sender=Patient)
def updatePatient(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.name = profile.name
        user.email = profile.email
        user.phone = profile.phone
        user.save()
        subject = 'Profile Information Updated'
        message = 'Hello ' + profile.name + '! Your profile information has been updated!'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


@receiver(post_delete, sender=Doctor)
def deleteDoctor(sender, instance, **kwargs):
    doctor = instance
    user = doctor.user
    user.delete()


@receiver(post_delete, sender=Patient)
def deletePatient(sender, instance, **kwargs):
    patient = instance
    user = patient.user
    user.delete()
