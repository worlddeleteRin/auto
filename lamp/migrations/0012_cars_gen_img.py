# Generated by Django 3.0.5 on 2020-07-09 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lamp', '0011_auto_20200708_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='gen_img',
            field=models.CharField(default='https://placehold.it/420x327', max_length=3000),
        ),
    ]