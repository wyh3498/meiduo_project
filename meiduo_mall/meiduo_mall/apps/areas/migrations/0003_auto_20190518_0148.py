# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-18 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0002_auto_20190518_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(max_length=20, verbose_name='名称'),
        ),
    ]
