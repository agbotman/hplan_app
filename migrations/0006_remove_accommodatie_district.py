# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 14:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hplan_app', '0005_transfer_accommodatie_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accommodatie',
            name='district',
        ),
    ]
