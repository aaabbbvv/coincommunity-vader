# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-12 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0019_tempcommunitygrow'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempMarketCapGrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_type', models.CharField(max_length=150)),
                ('value', models.FloatField()),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.Coin')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
