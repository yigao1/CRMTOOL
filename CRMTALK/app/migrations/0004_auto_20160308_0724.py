# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160308_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cell',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='direct',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='fax',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
