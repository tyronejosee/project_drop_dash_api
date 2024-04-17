# Generated by Django 5.0.4 on 2024-04-17 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('foods', '0002_alter_food_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='normal_price',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='food',
            name='description',
        ),
        migrations.RemoveField(
            model_name='food',
            name='preparation_time',
        ),
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='categories.category'),
        ),
        migrations.AlterField(
            model_name='food',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
