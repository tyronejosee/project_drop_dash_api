# Generated by Django 5.0.4 on 2024-05-20 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0003_driver_driver_license_driver_identification_document_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]