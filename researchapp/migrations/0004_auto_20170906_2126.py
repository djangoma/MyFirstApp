# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-06 15:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('researchapp', '0003_auto_20170905_1251'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Externalfundedproject',
            new_name='Externalfp',
        ),
        migrations.RenameModel(
            old_name='facultyinternalfundedproject',
            new_name='Facultyifp',
        ),
        migrations.RenameModel(
            old_name='studentinternalfundedproject',
            new_name='Studentifp',
        ),
        migrations.RenameField(
            model_name='facultyifp',
            old_name='principalinvestigator',
            new_name='pi',
        ),
        migrations.AlterField(
            model_name='journal',
            name='publishedon',
            field=models.DateField(default=datetime.datetime(2017, 9, 6, 15, 55, 55, 826162, tzinfo=utc), verbose_name='Published On'),
        ),
    ]
