# Generated by Django 4.2.6 on 2023-11-30 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stundentlogin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sturesponce',
            old_name='rollno',
            new_name='username',
        ),
    ]
