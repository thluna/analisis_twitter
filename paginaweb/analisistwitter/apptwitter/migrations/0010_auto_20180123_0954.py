# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-23 14:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptwitter', '0009_auto_20180123_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentoexcel',
            name='fechaingreso',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 23, 9, 54, 52, 196586)),
        ),
        migrations.AlterField(
            model_name='documentogoogle',
            name='fechaingreso',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 23, 9, 54, 52, 195678)),
        ),
    ]
