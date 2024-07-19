# Generated by Django 5.0.4 on 2024-07-19 19:24

import apps.utilities.paths
import apps.utilities.validators
import django.core.validators
import django.db.models.deletion
import simple_history.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalRestaurant',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('slug', models.SlugField(blank=True)),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('image', models.TextField(max_length=100)),
                ('banner', models.TextField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('specialty', models.CharField(choices=[('varied', 'Varied'), ('chilean', 'Chilean'), ('peruvian', 'Peruvian'), ('argentinian', 'Argentinian'), ('mexican', 'Mexican'), ('italian', 'Italian'), ('french', 'French'), ('japanese', 'Japanese'), ('chinese', 'Chinese'), ('indian', 'Indian'), ('thai', 'Thai'), ('spanish', 'Spanish'), ('russian', 'Russian'), ('moroccan', 'Moroccan'), ('korean', 'Korean'), ('turkish', 'Turkish')], default='varied', max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('phone', models.CharField(db_index=True, max_length=12, validators=[apps.utilities.validators.validate_phone])),
                ('website', models.URLField(blank=True, max_length=255)),
                ('is_open', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('banking_certificate', models.TextField(blank=True, max_length=100)),
                ('e_rut', models.TextField(blank=True, max_length=100)),
                ('legal_rep_email', models.EmailField(blank=True, max_length=254)),
                ('legal_rep_identity_document', models.TextField(blank=True, max_length=100)),
                ('legal_rep_power_of_attorney', models.TextField(blank=True, max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('city_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='locations.city')),
                ('country_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='locations.country')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('state_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='locations.state')),
                ('user_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical restaurant',
                'verbose_name_plural': 'historical restaurants',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('image', models.ImageField(upload_to=apps.utilities.paths.image_path)),
                ('banner', models.ImageField(blank=True, upload_to=apps.utilities.paths.image_banner_path)),
                ('description', models.TextField(blank=True)),
                ('specialty', models.CharField(choices=[('varied', 'Varied'), ('chilean', 'Chilean'), ('peruvian', 'Peruvian'), ('argentinian', 'Argentinian'), ('mexican', 'Mexican'), ('italian', 'Italian'), ('french', 'French'), ('japanese', 'Japanese'), ('chinese', 'Chinese'), ('indian', 'Indian'), ('thai', 'Thai'), ('spanish', 'Spanish'), ('russian', 'Russian'), ('moroccan', 'Moroccan'), ('korean', 'Korean'), ('turkish', 'Turkish')], default='varied', max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('phone', models.CharField(max_length=12, unique=True, validators=[apps.utilities.validators.validate_phone])),
                ('website', models.URLField(blank=True, max_length=255)),
                ('is_open', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('banking_certificate', models.FileField(blank=True, upload_to='documents/')),
                ('e_rut', models.FileField(blank=True, upload_to='documents/')),
                ('legal_rep_email', models.EmailField(blank=True, max_length=254)),
                ('legal_rep_identity_document', models.FileField(blank=True, upload_to='documents/')),
                ('legal_rep_power_of_attorney', models.FileField(blank=True, upload_to='documents/')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='locations.city')),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='locations.country')),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='locations.state')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'restaurant',
                'verbose_name_plural': 'restaurants',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalFood',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('image', models.TextField(max_length=100, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['webp']), apps.utilities.validators.FileSizeValidator(limit_mb=1), apps.utilities.validators.validate_food_image])),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('is_gluten_free', models.BooleanField(default=False)),
                ('is_spicy', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='restaurants.category')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('restaurant_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='restaurants.restaurant')),
            ],
            options={
                'verbose_name': 'historical food',
                'verbose_name_plural': 'historical foods',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('image', models.ImageField(upload_to=apps.utilities.paths.image_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['webp']), apps.utilities.validators.FileSizeValidator(limit_mb=1), apps.utilities.validators.validate_food_image])),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('is_gluten_free', models.BooleanField(default=False)),
                ('is_spicy', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='restaurants.category')),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='restaurants.restaurant')),
            ],
            options={
                'verbose_name': 'food',
                'verbose_name_plural': 'foods',
                'ordering': ['pk'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='restaurants.restaurant'),
        ),
    ]
