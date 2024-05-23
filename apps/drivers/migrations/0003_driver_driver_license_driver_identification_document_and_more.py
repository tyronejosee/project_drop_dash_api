# Generated by Django 5.0.4 on 2024-05-20 18:07

import apps.utilities.paths
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_resource'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='driver_license',
            field=models.FileField(default='', upload_to=apps.utilities.paths.docs_path, validators=[django.core.validators.FileExtensionValidator(['pdf', 'jpg'])]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='identification_document',
            field=models.FileField(default='', upload_to=apps.utilities.paths.docs_path, validators=[django.core.validators.FileExtensionValidator(['pdf', 'jpg'])]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='social_security_certificate',
            field=models.FileField(default='', upload_to=apps.utilities.paths.docs_path, validators=[django.core.validators.FileExtensionValidator(['pdf', 'jpg'])]),
            preserve_default=False,
        ),
    ]