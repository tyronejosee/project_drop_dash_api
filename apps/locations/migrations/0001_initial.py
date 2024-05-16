# Generated by Django 5.0.4 on 2024-05-16 21:14

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
                'ordering': ['pk'],
                'indexes': [models.Index(fields=['name'], name='locations_c_name_b70dbe_idx')],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.country')),
            ],
            options={
                'verbose_name': 'state',
                'verbose_name_plural': 'states',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.state')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
                'ordering': ['pk'],
            },
        ),
        migrations.AddIndex(
            model_name='state',
            index=models.Index(fields=['name'], name='locations_s_name_5adbc5_idx'),
        ),
        migrations.AddIndex(
            model_name='city',
            index=models.Index(fields=['name'], name='locations_c_name_5719ba_idx'),
        ),
    ]
