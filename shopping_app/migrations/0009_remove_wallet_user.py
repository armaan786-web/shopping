# Generated by Django 4.1.5 on 2023-01-20 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0008_alter_booking_daily_wise_commission_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallet',
            name='user',
        ),
    ]