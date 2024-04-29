# Generated by Django 5.0.4 on 2024-04-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_actual_delivery_time_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['pk'], 'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['pk'], 'verbose_name': 'order_item', 'verbose_name_plural': 'order_items'},
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='count',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='tax',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=10),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10),
        ),
    ]