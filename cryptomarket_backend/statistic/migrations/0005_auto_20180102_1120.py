# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-02 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0004_auto_20171219_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rankingstatistic',
            name='growth_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='growth_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='growth_six_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='growth_three_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='growth_week',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='growth_year_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='overall_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='overall_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='overall_six_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='overall_three_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='overall_week',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='overall_year_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='trending_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='trending_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='trending_six_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='trending_three_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='trending_week',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rankingstatistic',
            name='trending_year_month',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
