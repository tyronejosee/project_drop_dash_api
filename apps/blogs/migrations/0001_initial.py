# Generated by Django 5.0.4 on 2024-05-13 17:22

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
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('content', models.TextField()),
                ('is_featured', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='blogs.tag')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'ordering': ['pk'],
            },
        ),
    ]
