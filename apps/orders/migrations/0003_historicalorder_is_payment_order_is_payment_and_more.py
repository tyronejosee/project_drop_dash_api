# Generated by Django 5.0.4 on 2024-07-29 17:05

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_historicalorder_amount_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorder',
            name='is_payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='is_payment',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='OrderRating',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rating', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('comment', models.TextField(blank=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_ratings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'order rating',
                'verbose_name_plural': 'order ratings',
            },
        ),
        migrations.CreateModel(
            name='OrderReport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reason', models.CharField(help_text='Short description of the reason for reporting', max_length=50)),
                ('description', models.TextField(blank=True, help_text='Detailed description of the issue')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('resolved', 'Resolved'), ('rejected', 'Rejected'), ('closed', 'Closed')], default='pending', max_length=20)),
                ('is_resolved', models.BooleanField(default=False)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_reports', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'order report',
                'verbose_name_plural': 'order reports',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddConstraint(
            model_name='orderrating',
            constraint=models.UniqueConstraint(fields=('order_id', 'user_id'), name='unique_order_user_rating'),
        ),
        migrations.AddIndex(
            model_name='orderreport',
            index=models.Index(fields=['is_resolved'], name='orders_orde_is_reso_5ba8d6_idx'),
        ),
        migrations.AddConstraint(
            model_name='orderreport',
            constraint=models.UniqueConstraint(fields=('order_id', 'user_id'), name='unique_order_user_report'),
        ),
    ]
