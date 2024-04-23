# Generated by Django 5.0.4 on 2024-04-17 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FixedDiscountCoupon',
            new_name='FixedCoupon',
        ),
        migrations.RenameModel(
            old_name='PercentageDiscountCoupon',
            new_name='PercentageCoupon',
        ),
        migrations.AlterModelOptions(
            name='fixedcoupon',
            options={'verbose_name': 'fixed coupon', 'verbose_name_plural': 'fixed coupons'},
        ),
        migrations.AlterModelOptions(
            name='percentagecoupon',
            options={'verbose_name': 'percentage coupon', 'verbose_name_plural': 'percentage coupons'},
        ),
    ]