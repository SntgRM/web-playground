# Generated by Django 5.1 on 2024-09-04 22:01

import registration.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=registration.models.custom_uploar_to),
        ),
    ]