# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 13:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hplan_app', '0011_auto_20160804_1308'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='accdescription',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='accdescription',
            name='language',
        ),
    ]
