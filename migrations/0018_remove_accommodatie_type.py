# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-13 12:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hplan_app', '0017_link_accommodatie_type_fk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accommodatie',
            name='type',
        ),
    ]
