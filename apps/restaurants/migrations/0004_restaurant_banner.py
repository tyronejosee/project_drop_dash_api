# Generated by Django 5.0.4 on 2024-04-18 16:37

import apps.utilities.paths
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_alter_restaurant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='banner',
            field=models.ImageField(blank=True, upload_to=apps.utilities.paths.image_banner_path),
        ),
    ]