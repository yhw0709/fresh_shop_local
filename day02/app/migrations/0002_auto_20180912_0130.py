# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-12 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student2',
            name='chinese',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='student2',
            name='math',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
