# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-16 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parlamentares', '0025_frente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frente',
            name='data_extincao',
            field=models.DateField(blank=True, null=True, verbose_name='Data Dissolução'),
        ),
    ]
