# Generated by Django 4.2.6 on 2023-11-26 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_registration_aadhar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='status',
        ),
    ]
