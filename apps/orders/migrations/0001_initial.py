# Generated by Django 5.0.4 on 2024-07-19 19:24

import apps.utilities.validators
import django.db.models.deletion
import simple_history.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
        ('restaurants', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalOrder',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('shipping_name', models.CharField(max_length=255)),
                ('shipping_phone', models.CharField(db_index=True, max_length=12, validators=[apps.utilities.validators.validate_phone])),
                ('shipping_time', models.CharField(max_length=255)),
                ('shipping_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('transaction', models.CharField(db_index=True, editable=False, max_length=255)),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255)),
                ('note', models.TextField(blank=True)),
                ('zip_code', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('not_processed', 'Not Processed'), ('processed', 'Processed'), ('shipping', 'Shipping'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='not_processed', max_length=50)),
                ('payment_method', models.CharField(choices=[('cash', 'Cash'), ('bank transfer', 'Bank Transfer'), ('credit card', 'Credit Card'), ('debit card', 'Debit Card')], default='bank transfer', max_length=15)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('city_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='locations.city')),
                ('country_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='locations.country')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('restaurant_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='restaurants.restaurant')),
                ('state_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='locations.state')),
                ('user_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical order',
                'verbose_name_plural': 'historical orders',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shipping_name', models.CharField(max_length=255)),
                ('shipping_phone', models.CharField(max_length=12, unique=True, validators=[apps.utilities.validators.validate_phone])),
                ('shipping_time', models.CharField(max_length=255)),
                ('shipping_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('transaction', models.CharField(editable=False, max_length=255, unique=True)),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255)),
                ('note', models.TextField(blank=True)),
                ('zip_code', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('not_processed', 'Not Processed'), ('processed', 'Processed'), ('shipping', 'Shipping'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='not_processed', max_length=50)),
                ('payment_method', models.CharField(choices=[('cash', 'Cash'), ('bank transfer', 'Bank Transfer'), ('credit card', 'Credit Card'), ('debit card', 'Debit Card')], default='bank transfer', max_length=15)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='locations.city')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='locations.country')),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.restaurant')),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='locations.state')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.food')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'verbose_name': 'order item',
                'verbose_name_plural': 'order items',
                'ordering': ['pk'],
            },
        ),
    ]
