# Generated by Django 3.0.5 on 2020-07-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lamp', '0013_auto_20200711_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.CharField(default='https://placehold.it/50x50', max_length=3000),
        ),
    ]