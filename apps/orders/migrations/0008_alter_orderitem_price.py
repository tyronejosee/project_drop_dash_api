# Generated by Django 5.0.4 on 2024-08-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_orderitem_unique_order_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, help_text='The reference unit price of the product.', max_digits=10),
        ),
    ]
