# Generated by Django 2.2.18 on 2022-02-10 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_name', models.CharField(max_length=1000)),
                ('details', models.CharField(max_length=10000)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]