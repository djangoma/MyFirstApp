# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-05 07:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('researchapp', '0002_auto_20170904_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='publishedon',
            field=models.DateField(default=datetime.datetime(2017, 9, 5, 7, 21, 4, 396897, tzinfo=utc), verbose_name='Published On'),
        ),
    ]
