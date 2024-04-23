# Generated by Django 5.0.4 on 2024-04-17 18:48

import apps.utilities.paths
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_facebook_restaurant_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(upload_to=apps.utilities.paths.image_path),
        ),
    ]