# Generated by Django 5.0.4 on 2024-05-22 16:25

import apps.utilities.paths
import apps.utilities.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(upload_to=apps.utilities.paths.image_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['webp']), apps.utilities.validators.FileSizeValidator(limit_mb=1), apps.utilities.validators.validate_food_image]),
        ),
    ]