# Generated by Django 3.2.9 on 2022-01-03 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0006_auto_20220102_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
