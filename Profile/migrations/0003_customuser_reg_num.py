# Generated by Django 3.2.9 on 2021-12-20 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_allergies_degree_doctor_patient_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='reg_num',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
