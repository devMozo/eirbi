# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-26 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_fechaalq_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='tarifaDiaria',
            field=models.IntegerField(default=0),
        ),
    ]
