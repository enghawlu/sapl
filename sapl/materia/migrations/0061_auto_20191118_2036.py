# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-11-18 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0060_auto_20190905_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentoacessorio',
            name='autor',
            field=models.CharField(blank=True, max_length=200, verbose_name='Autor'),
        ),
    ]