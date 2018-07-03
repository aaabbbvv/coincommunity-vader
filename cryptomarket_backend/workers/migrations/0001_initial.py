# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-18 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Coin')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('scrapper', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('resource_url', models.URLField(blank=True, max_length=800, null=True)),
                ('info', models.TextField(blank=True, null=True, verbose_name='Json helper info')),
                ('priority', models.CharField(choices=[(1, 'High priority'), (2, 'Normal priority'), (3, 'Low priority')], default=2, max_length=100)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='workers.Coin')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
