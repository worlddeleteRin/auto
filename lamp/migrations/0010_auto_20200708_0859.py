# Generated by Django 3.0.5 on 2020-07-08 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lamp', '0009_auto_20200708_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lamps',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lamp.Destination'),
        ),
    ]
