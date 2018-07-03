# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-18 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0002_auto_20171218_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='priority',
            field=models.IntegerField(choices=[(1, 'High priority'), (2, 'Normal priority'), (3, 'Low priority')], default=2),
        ),
    ]
