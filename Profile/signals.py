from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Doctor, Patient


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


@receiver(post_delete, sender=Doctor)
def deleteDoctor(sender, instance, **kwargs):
    user = instance
    user.delete()


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


@receiver(post_save, sender=Patient)
def updatePatient(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if not created:
        user.name = profile.name
        user.email = profile.email
        user.phone = profile.phone
        user.save()


@receiver(post_delete, sender=Patient)
def deletePatient(sender, instance, **kwargs):
    user = instance
    user.delete()
