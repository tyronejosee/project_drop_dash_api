# Generated by Django 5.0.4 on 2024-04-09 17:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='restaurants/')),
                ('description', models.TextField(blank=True)),
                ('specialty', models.CharField(choices=[('varied', 'Varied'), ('chilean', 'Chilean'), ('peruvian', 'Peruvian'), ('argentinian', 'Argentinian'), ('mexican', 'Mexican'), ('italian', 'Italian'), ('french', 'French'), ('japanese', 'Japanese'), ('chinese', 'Chinese'), ('indian', 'Indian'), ('thai', 'Thai'), ('spanish', 'Spanish'), ('russian', 'Russian'), ('moroccan', 'Moroccan'), ('korean', 'Korean'), ('turkish', 'Turkish')], default='varied', max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('website', models.URLField(blank=True, max_length=255)),
                ('is_open', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Restaurant',
                'verbose_name_plural': 'Restaurants',
            },
        ),
    ]