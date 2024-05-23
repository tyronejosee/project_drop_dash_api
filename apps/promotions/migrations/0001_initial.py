# Generated by Django 5.0.4 on 2024-05-23 22:29

import apps.promotions.validators
import apps.utilities.paths
import apps.utilities.validators
import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FixedCoupon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(blank=True, max_length=36, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('is_active', models.BooleanField(default=True)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=7, validators=[apps.promotions.validators.validate_discount_price])),
            ],
            options={
                'verbose_name': 'fixed coupon',
                'verbose_name_plural': 'fixed coupons',
            },
        ),
        migrations.CreateModel(
            name='PercentageCoupon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(blank=True, max_length=36, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('is_active', models.BooleanField(default=True)),
                ('discount_percentage', models.IntegerField(validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(25)])),
            ],
            options={
                'verbose_name': 'percentage coupon',
                'verbose_name_plural': 'percentage coupons',
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('conditions', models.TextField()),
                ('start_date', models.DateField(verbose_name=apps.utilities.validators.DateRangeValidator(days=90))),
                ('end_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to=apps.utilities.paths.image_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['webp']), apps.utilities.validators.FileSizeValidator(limit_mb=1)])),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'promotion',
                'verbose_name_plural': 'promotions',
                'ordering': ['pk'],
            },
        ),
    ]
