# Generated by Django 4.1.5 on 2023-01-18 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0003_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='commision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commision', models.IntegerField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_app.booking')),
            ],
        ),
    ]
