# Generated by Django 3.0.5 on 2020-07-14 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lamp', '0014_auto_20200711_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='mark_norm',
            field=models.CharField(default='-', max_length=100),
        ),
    ]
