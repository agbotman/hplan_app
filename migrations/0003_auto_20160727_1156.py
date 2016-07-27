# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hplan_app', '0002_auto_20160720_1942'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accommodatiebeheerder',
            options={'verbose_name': 'property manager', 'verbose_name_plural': 'propertymanagers'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['name'], 'verbose_name': 'country', 'verbose_name_plural': 'countries'},
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='aantaldagen',
            field=models.IntegerField(blank=True, db_column='AantalDagen', null=True, verbose_name='number of days'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='acc_intro',
            field=models.TextField(blank=True, db_column='Acc_Intro', null=True, verbose_name='property introduction'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='acc_intro_de',
            field=models.TextField(blank=True, db_column='Acc_Intro_DE', null=True, verbose_name='property introduction (German)'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='acc_intro_fr',
            field=models.TextField(blank=True, db_column='Acc_Intro_FR', null=True, verbose_name='property introduction (French)'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='acc_intro_nl',
            field=models.TextField(blank=True, db_column='Acc_Intro_NL', null=True, verbose_name='property introduction (Dutch)'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='accaddsort',
            field=models.IntegerField(blank=True, db_column='AccAddSort', null=True, verbose_name='addition accommodation kind'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='address',
            field=models.CharField(blank=True, db_column='AccAddress', max_length=50, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='beheerder',
            field=models.ForeignKey(blank=True, db_column='AccBehID', null=True, on_delete=django.db.models.deletion.CASCADE, to='hplan_app.AccommodatieBeheerder', verbose_name='property manager'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='bground',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='bground'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='cdate',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='cdate'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='city',
            field=models.CharField(blank=True, db_column='AccPlace', max_length=50, null=True, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hplan_app.Country', verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='datumgewijzigd',
            field=models.DateTimeField(blank=True, db_column='DatumGewijzigd', null=True, verbose_name='date last changed'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='datumonline',
            field=models.DateTimeField(db_column='DatumOnline', verbose_name='date online'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='datumtoegevoegd',
            field=models.DateTimeField(db_column='DatumToegevoegd', verbose_name='introduction date'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='district',
            field=models.IntegerField(db_column='AccDistrict', verbose_name='district'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='gebruikreserveringen',
            field=models.BooleanField(db_column='GebruikReserveringen', verbose_name='users can reserve'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='ground',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='ground'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='homepage',
            field=models.CharField(blank=True, db_column='AccHomepage', max_length=200, null=True, verbose_name='homepage'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='picturefront',
            field=models.IntegerField(blank=True, db_column='Acc_PictureFront', null=True, verbose_name='front picture'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='places',
            field=models.IntegerField(db_column='AccNmbSPlac', verbose_name='number of places'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='publicreserveringen',
            field=models.BooleanField(db_column='PublicReserveringen', verbose_name='public can reserve'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='rooms',
            field=models.IntegerField(db_column='AccNmbRooms', verbose_name='number of rooms'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='sort',
            field=models.IntegerField(db_column='AccSort', verbose_name='accommodation kind'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='status',
            field=models.BooleanField(verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='teller1',
            field=models.IntegerField(blank=True, null=True, verbose_name='teller1'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='type',
            field=models.IntegerField(db_column='AccType', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='verkoopprijs',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='selling price'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='vz1',
            field=models.BooleanField(db_column='Acc_vz1', verbose_name='pets allowed'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='vz2',
            field=models.BooleanField(db_column='Acc_vz2', verbose_name='smoking not allowed'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='vz3',
            field=models.BooleanField(db_column='Acc_vz3', verbose_name='swimming pool'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='vz4',
            field=models.BooleanField(db_column='Acc_vz4', verbose_name='kitchen'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='vz5',
            field=models.BooleanField(db_column='Acc_vz5', verbose_name='pets allowed'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='vz6',
            field=models.BooleanField(db_column='Acc_vz6', verbose_name='laundry facility'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='vz7',
            field=models.BooleanField(db_column='Acc_vz7', verbose_name='handicapped'),
        ),
        migrations.AlterField(
            model_name='accommodatie',
            name='zipcode',
            field=models.CharField(blank=True, db_column='AccZip', max_length=10, null=True, verbose_name='zip code'),
        ),
        migrations.AlterField(
            model_name='accommodatiebeheerder',
            name='address',
            field=models.CharField(blank=True, db_column='Address', max_length=100, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='accommodatiebeheerder',
            name='city',
            field=models.CharField(blank=True, db_column='Place', max_length=50, null=True, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='accommodatiebeheerder',
            name='contact_de',
            field=models.NullBooleanField(db_column='Contact_DE', verbose_name='German speaking'),
        ),
        migrations.AlterField(
            model_name='accommodatiebeheerder',
            name='contact_en',
            field=models.NullBooleanField(db_column='Contact_EN', verbose_name='English speaking'),
        ),
        migrations.AlterField(
            model_name='accommodatiebeheerder',
            name='contact_fr',
            field=models.NullBooleanField(db_column='Contact_FR', verbose_name='French speaking'),
        ),
        migrations.AlterField(
            model_name='accommodatiebeheerder',
            name='contact_nl',
            field=models.NullBooleanField(db_column='Contact_NL', verbose_name='Dutch speaking'),
        ),
        migrations.AlterField(
            model_name='accommodatiebeheerder',
            name='country',
            field=models.CharField(blank=True, db_column='Country', max_length=20, null=True, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='accommodatiebeheerder',
            name='datumgeregistreerd',
            field=models.DateTimeField(db_column='DatumGeregistreerd', verbose_name='registration date'),
        ),
        migrations.AlterField(
            model_name='accommodatiebeheerder',
            name='datumgewijzigd',
            field=models.DateTimeField(blank=True, db_column='DatumGewijzigd', null=True, verbose_name='last change date'),
        ),
        migrations.AlterField(
            model_name='accommodatiebeheerder',
            name='fax',
            field=models.CharField(blank=True, db_column='Fax', max_length=20, null=True, verbose_name='fax'),
        ),
        migrations.AlterField(
            model_name='accommodatiebeheerder',
            name='fullname',
            field=models.CharField(db_column='FullName', max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='accommodatiebeheerder',
            name='mobile',
            field=models.CharField(blank=True, db_column='MobPhone', max_length=20, null=True, verbose_name='mobile'),
        ),
        migrations.AlterField(
            model_name='accommodatiebeheerder',
            name='telephone',
            field=models.CharField(blank=True, db_column='Telephone', max_length=20, null=True, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='accommodatiebeheerder',
            name='zip',
            field=models.CharField(blank=True, db_column='Zip', max_length=10, null=True, verbose_name='zipcode'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=40, unique=True, verbose_name='name'),
        ),
    ]