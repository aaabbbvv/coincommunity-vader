# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-28 09:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0028_tempvaluebyperiod'),
        ('parsers', '0030_auto_20180212_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='GitHubDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('forks', models.IntegerField(null=True, verbose_name='Forks')),
                ('stars', models.IntegerField(null=True, verbose_name='Stars')),
                ('watchers', models.IntegerField(null=True, verbose_name='Watchers')),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.Coin')),
            ],
            options={
                'verbose_name': 'GitHubDetails Data',
                'verbose_name_plural': 'GitHubDetails Data',
            },
        ),
    ]
