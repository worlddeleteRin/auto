# Generated by Django 3.0.5 on 2020-07-02 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lamp', '0005_lamps_imgsrc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lamps',
            name='imgsrc',
            field=models.CharField(default='https://placehold.it/155x155', max_length=2000),
        ),
    ]
