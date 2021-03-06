# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-29 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0006_statisticparser_is_calculating'),
        ('parsers', '0022_auto_20171228_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketcapData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Date')),
                ('open', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('high', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('low', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('close', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('volume', models.BigIntegerField(blank=True, null=True)),
                ('market_cap', models.BigIntegerField(null=True)),
                ('coin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marketcap', to='workers.Coin')),
            ],
            options={
                'verbose_name': 'Marketcap Data',
                'verbose_name_plural': 'Marketcap Data',
            },
        ),
    ]
