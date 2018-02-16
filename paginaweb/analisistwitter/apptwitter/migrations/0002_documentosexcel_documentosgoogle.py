# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-23 14:23
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apptwitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentosExcel',
            fields=[
                ('id_documentoexcel', models.AutoField(primary_key=True, serialize=False)),
                ('fechaingreso', models.DateTimeField(default=datetime.datetime(2018, 1, 23, 9, 23, 15, 253150))),
                ('archivo', models.FileField(blank=True, upload_to='archivos')),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentosGoogle',
            fields=[
                ('id_documentogoogle', models.AutoField(primary_key=True, serialize=False)),
                ('fechaingreso', models.DateTimeField(default=datetime.datetime(2018, 1, 23, 9, 23, 15, 251895))),
                ('archivo_key', models.CharField(max_length=450)),
                ('usuario', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
