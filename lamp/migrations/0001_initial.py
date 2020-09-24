# Generated by Django 3.0.5 on 2020-07-01 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('gen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LampType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lamps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.IntegerField(default=0)),
                ('brand', models.CharField(max_length=100)),
                ('cars', models.ManyToManyField(to='lamp.Cars')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lamp.Category')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lamp.Destination')),
                ('ltype', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lamp.LampType')),
            ],
        ),
    ]
