# Generated by Django 5.0.4 on 2024-07-29 19:37

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
        ('orders', '0003_historicalorder_is_payment_order_is_payment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverAssignment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.driver')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'verbose_name': 'resource',
                'verbose_name_plural': 'resources',
                'ordering': ['-assigned_at'],
            },
        ),
    ]
