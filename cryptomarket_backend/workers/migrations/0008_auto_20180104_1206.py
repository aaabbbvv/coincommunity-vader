# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-04 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0007_auto_20171229_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempCommunityRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('time_type', models.CharField(max_length=150)),
                ('rating_type', models.CharField(choices=[('overall', 'overall'), ('growth', 'growth'), ('trending', 'trending')], max_length=20)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.Coin')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TempRedditFollowerRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('time_type', models.CharField(max_length=150)),
                ('rating_type', models.CharField(choices=[('overall', 'overall'), ('growth', 'growth'), ('trending', 'trending')], max_length=20)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.Coin')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TempTwitterFollowerRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('time_type', models.CharField(max_length=150)),
                ('rating_type', models.CharField(choices=[('overall', 'overall'), ('growth', 'growth'), ('trending', 'trending')], max_length=20)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workers.Coin')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='worker',
            name='scrapper',
            field=models.CharField(choices=[('twitter_comments_vader', 'Twitter comments for vader'), ('twitter_comments', 'Twitter comments'), ('twitter_likes', 'Twitter likes'), ('twitter_followers', 'Twitter followers'), ('twitter_text', 'Twitter text'), ('reddit_subscribers', 'Reddit subscribers'), ('github_parser', 'Github repository creations number'), ('marketcap_scraper', 'Marketcap Scrapper')], max_length=255),
        ),
    ]
