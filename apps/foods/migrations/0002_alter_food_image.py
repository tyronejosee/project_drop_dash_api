# Generated by Django 5.0.4 on 2024-04-17 17:30

import apps.utilities.paths
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(upload_to=apps.utilities.paths.image_path),
        ),
    ]