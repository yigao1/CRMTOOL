# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 11:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160308_0442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='id',
        ),
        migrations.AddField(
            model_name='note',
            name='lead',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.Lead'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lead',
            name='company',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]