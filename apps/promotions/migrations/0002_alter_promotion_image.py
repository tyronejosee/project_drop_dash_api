# Generated by Django 5.0.4 on 2024-05-13 22:55

import apps.utilities.paths
import apps.utilities.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='image',
            field=models.ImageField(upload_to=apps.utilities.paths.image_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['webp']), apps.utilities.validators.FileSizeValidator(limit_mb=2)]),
        ),
    ]