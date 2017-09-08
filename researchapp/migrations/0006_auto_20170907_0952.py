# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-07 04:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('researchapp', '0005_auto_20170907_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalfp',
            name='copi',
            field=models.CharField(blank=True, max_length=100, verbose_name='Co-PI'),
        ),
        migrations.AlterField(
            model_name='facultyifp',
            name='copi',
            field=models.CharField(blank=True, max_length=100, verbose_name='Co-PI'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='publishedon',
            field=models.DateField(default=datetime.datetime(2017, 9, 7, 4, 22, 55, 113952, tzinfo=utc), verbose_name='Published On'),
        ),
        migrations.AlterField(
            model_name='studentifp',
            name='copi',
            field=models.CharField(blank=True, max_length=100, verbose_name='Co-PI'),
        ),
    ]