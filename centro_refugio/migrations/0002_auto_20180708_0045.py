# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-08 00:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centro_refugio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centro',
            name='visita',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adopcion.Persona'),
        ),
    ]