# Generated by Django 4.1.5 on 2023-01-21 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0002_remove_wallet_user_wallet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='user',
            field=models.ManyToManyField(related_name='wallet_set', to='shopping_app.booking'),
        ),
    ]