# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-06 06:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('norma', '0019_auto_20190104_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normajuridica',
            name='data_publicacao',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Publicação'),
        ),
        migrations.AlterField(
            model_name='normajuridica',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='norma.TipoNormaJuridica', verbose_name='Tipo da Norma Jurídica'),
        ),
        migrations.AlterField(
            model_name='normajuridica',
            name='veiculo_publicacao',
            field=models.CharField(blank=True, max_length=30, verbose_name='Veículo de Publicação'),
        ),
    ]