# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hplan_app', '0003_auto_20160727_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodatie',
            name='district_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hplan_app.District'),
        ),
    ]
