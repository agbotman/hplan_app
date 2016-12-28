# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-13 12:16
from __future__ import unicode_literals

from django.db import migrations

def link_accommodatietype(apps, schema_editor):
    Accommodatie = apps.get_model('hplan_app', 'Accommodatie')
    for acc in Accommodatie.objects.all():
        try:
            acc.type_fk_id = acc.type
            acc.save()
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('hplan_app', '0016_accommodatie_type_fk'),
    ]

    operations = [
        migrations.RunPython(link_accommodatietype),
    ]