# Generated by Django 3.0.8 on 2020-09-13 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20200913_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cart',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.Cart'),
        ),
    ]
