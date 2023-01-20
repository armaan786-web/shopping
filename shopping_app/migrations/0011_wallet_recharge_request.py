# Generated by Django 4.1.5 on 2023-01-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0010_remove_wallet_booking_wallet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='recharge_request',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Reject', 'Reject')], default='Pending', max_length=50),
        ),
    ]