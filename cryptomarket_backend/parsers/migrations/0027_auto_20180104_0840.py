# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-04 08:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsers', '0026_auto_20180103_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='github',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 4, 8, 40, 45, 929456)),
        ),
    ]
