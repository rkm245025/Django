# Generated by Django 4.2.6 on 2023-11-26 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='username',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]