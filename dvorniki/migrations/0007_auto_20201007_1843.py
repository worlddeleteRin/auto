# Generated by Django 3.0.8 on 2020-10-07 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvorniki', '0006_auto_20201007_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvcar',
            name='gen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dvorniki.Dvgen'),
        ),
        migrations.AlterField(
            model_name='dvcar',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dvorniki.Dvmark'),
        ),
        migrations.AlterField(
            model_name='dvcar',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dvorniki.Dvmodel'),
        ),
        migrations.AlterField(
            model_name='dvgen',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dvorniki.Dvmark'),
        ),
        migrations.AlterField(
            model_name='dvgen',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dvorniki.Dvmodel'),
        ),
    ]
