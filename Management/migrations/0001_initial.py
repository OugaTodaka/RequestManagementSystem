# Generated by Django 4.2.6 on 2024-07-08 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=100)),
                ('system_name', models.CharField(max_length=30)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RequestFunction',
            fields=[
                ('function_id', models.AutoField(primary_key=True, serialize=False)),
                ('function_name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=400)),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.request')),
            ],
        ),
    ]
