from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models


class AccDescription(models.Model):
    accommodatie = models.ForeignKey('Accommodatie', db_column='AccID')
    language = models.IntegerField(db_column='AccLanguage')
    description = models.TextField(_('description'), db_column='AccDescription', blank=True, null=True)  
    updatedtime = models.DateTimeField(_('date last changed'), db_column='AccUpdatedTime')  

    class Meta:
        db_table = 'acc_description'
        verbose_name = _('accommodation description')
        verbose_name_plural = _('accommodation descriptions')
        unique_together = ('accommodatie', 'language')

    def __unicode__(self):
        return '%s, %s, %s' % (self.accommodatie.address, self.accommodatie.city, self.accommodatie.country)


class Accbehonuser(models.Model):
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    accbehid = models.IntegerField(db_column='AccBehID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'accbehonuser'


class Accommodatie(models.Model):
    accid = models.AutoField(db_column='AccID', primary_key=True)  
    beheerder = models.ForeignKey('AccommodatieBeheerder', blank=True, null=True, db_column='AccBehID',
                                  verbose_name=_('property manager'))
    type = models.IntegerField(_('type'), db_column='AccType')
    address = models.CharField(_('address'), db_column='AccAddress', max_length=50, blank=True, null=True)  
    zipcode = models.CharField(_('zip code'), db_column='AccZip', max_length=10, blank=True, null=True)  
    city = models.CharField(_('city'), db_column='AccPlace', max_length=50, blank=True, null=True)
    country = models.ForeignKey('Country', verbose_name=_('country'))
    district = models.ForeignKey('District', blank=True, null=True)
    rooms = models.IntegerField(_('number of rooms'), db_column='AccNmbRooms')  
    places = models.IntegerField(_('number of places'), db_column='AccNmbSPlac')  
    homepage = models.CharField(_('homepage'), db_column='AccHomepage', max_length=200, blank=True, null=True)  
    vz1 = models.BooleanField(_('pets allowed'), db_column='Acc_vz1') 
    vz2 = models.BooleanField(_('smoking not allowed'), db_column='Acc_vz2')  
    vz3 = models.BooleanField(_('swimming pool'), db_column='Acc_vz3')  
    vz4 = models.BooleanField(_('kitchen'), db_column='Acc_vz4')  
    vz5 = models.BooleanField(_('pets allowed'), db_column='Acc_vz5')  
    vz6 = models.BooleanField(_('laundry facility'), db_column='Acc_vz6')  
    vz7 = models.BooleanField(_('handicapped'), db_column='Acc_vz7')  
    vz8 = models.BooleanField(db_column='Acc_vz8')  
    picturefront = models.IntegerField(_('front picture'), db_column='Acc_PictureFront', blank=True, null=True)  
    acc_intro = models.TextField(_('property introduction'), db_column='Acc_Intro', blank=True, null=True)  
    acc_intro_nl = models.TextField(_('property introduction (Dutch)'), db_column='Acc_Intro_NL', blank=True, null=True)  
    acc_intro_de = models.TextField(_('property introduction (German)'), db_column='Acc_Intro_DE', blank=True, null=True)  
    acc_intro_fr = models.TextField(_('property introduction (French)'), db_column='Acc_Intro_FR', blank=True, null=True)  
    status = models.BooleanField(_('status'), )
    datumtoegevoegd = models.DateTimeField(_('introduction date'), db_column='DatumToegevoegd')  
    datumgewijzigd = models.DateTimeField(_('date last changed'), db_column='DatumGewijzigd', blank=True, null=True)  
    datumonline = models.DateTimeField(_('date online'), db_column='DatumOnline')  
    sort = models.IntegerField(_('accommodation kind'), db_column='AccSort')  
    gebruikreserveringen = models.BooleanField(_('users can reserve'), db_column='GebruikReserveringen')  
    publicreserveringen = models.BooleanField(_('public can reserve'), db_column='PublicReserveringen')  
    aantaldagen = models.IntegerField(_('number of days'), db_column='AantalDagen', blank=True, null=True)  
    accaddsort = models.IntegerField(_('addition accommodation kind'), db_column='AccAddSort', blank=True, null=True)  
    verkoopprijs = models.CharField(_('selling price'), max_length=15, blank=True, null=True)
    ground = models.CharField(_('ground'), max_length=10, blank=True, null=True)
    bground = models.CharField(_('bground'), max_length=10, blank=True, null=True)
    cdate = models.CharField(_('cdate'), max_length=10, blank=True, null=True)
    teller1 = models.IntegerField(_('teller1'), blank=True, null=True)

    class Meta:
        db_table = 'accommodatie'
        verbose_name = _('accommodation')
        verbose_name_plural = _('accommodations')

    def __unicode__(self):
        return '%s, %s, %s' % (self.address, self.city, self.country)


class AccommodatieBeheerder(models.Model):
    accbehid = models.AutoField(db_column='AccBehID', primary_key=True)  
    fullname = models.CharField(_('name'), db_column='FullName', max_length=50)  
    address = models.CharField(_('address'), db_column='Address', max_length=100, blank=True, null=True)  
    zip = models.CharField(_('zipcode'), db_column='Zip', max_length=10, blank=True, null=True)  
    city = models.CharField(_('city'), db_column='Place', max_length=50, blank=True, null=True)  
    country = models.CharField(_('country'), db_column='Country', max_length=20, blank=True, null=True)  
    telephone = models.CharField(_('phone'), db_column='Telephone', max_length=20, blank=True, null=True)  
    fax = models.CharField(_('fax'), db_column='Fax', max_length=20, blank=True, null=True)  
    mobile = models.CharField(_('mobile'), db_column='MobPhone', max_length=20, blank=True, null=True)  
    datumgeregistreerd = models.DateTimeField(_('registration date'), db_column='DatumGeregistreerd')  
    datumgewijzigd = models.DateTimeField(_('last change date'), db_column='DatumGewijzigd', blank=True, null=True)  
    contact_en = models.NullBooleanField(_('English speaking'), db_column='Contact_EN', blank=True, null=True)  
    contact_nl = models.NullBooleanField(_('Dutch speaking'), db_column='Contact_NL', blank=True, null=True)  
    contact_de = models.NullBooleanField(_('German speaking'), db_column='Contact_DE', blank=True, null=True)  
    contact_fr = models.NullBooleanField(_('French speaking'), db_column='Contact_FR', blank=True, null=True)  

    class Meta:
        db_table = 'accommodatie_beheerder'
        verbose_name = _('property manager')
        verbose_name_plural = _('propertymanagers')

    def __unicode__(self):
        return self.fullname


class AccommodatiePictures(models.Model):
    pictureid = models.AutoField(db_column='PictureID', primary_key=True)  
    picturetext = models.CharField(db_column='PictureText', max_length=100, blank=True, null=True)  
    picturetext_nl = models.CharField(db_column='PictureText_NL', max_length=100, blank=True, null=True)  
    picturetext_de = models.CharField(db_column='PictureText_DE', max_length=100, blank=True, null=True)  
    picturetext_fr = models.CharField(db_column='PictureText_FR', max_length=100, blank=True, null=True)  
    pictureext = models.CharField(db_column='PictureExt', max_length=4)  
    accommodatie = models.ForeignKey('Accommodatie', db_column='AccID')
    beheerder = models.ForeignKey('AccommodatieBeheerder', db_column='AccBehID', blank=True, null=True)
    pictureaccid = models.IntegerField(db_column='PictureAccID', blank=True, null=True)  

    class Meta:
        db_table = 'accommodatie_pictures'


class RegionLinks(models.Model):
    linkid = models.AutoField(db_column='LinkID', primary_key=True)  
    countryid = models.IntegerField(db_column='CountryID', blank=True, null=True)  
    regionid = models.IntegerField(db_column='RegionID', blank=True, null=True)  
    languageid = models.IntegerField(db_column='LanguageID', blank=True, null=True)  
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  
    clicks = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'region_links'


class RegionText(models.Model):
    countryid = models.IntegerField(db_column='CountryID', blank=True, null=True)  
    regionid = models.IntegerField(db_column='RegionID', blank=True, null=True)  
    languageid = models.IntegerField(db_column='LanguageID', blank=True, null=True)  
    text = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'region_text'


class Users(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  
    username = models.CharField(db_column='UserName', max_length=25, blank=True, null=True)  
    password = models.CharField(db_column='UserPassword', max_length=20, blank=True, null=True)  
    emailadres = models.CharField(db_column='Emailadres', max_length=160, blank=True, null=True)  
    active = models.NullBooleanField(db_column='Active', blank=True, null=True)  
    activatiecode = models.CharField(max_length=8, blank=True, null=True)
    lastlogin = models.DateTimeField(db_column='LastLogin', blank=True, null=True)

    class Meta:
        db_table = 'users'

     
class Country(models.Model):
    countryid = models.IntegerField(unique=True)
    name = models.CharField(_('name'), max_length=40, unique=True)
    
    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')
        ordering = ['name']

    def __unicode__(self):
        return self.name
     
class District(models.Model):
    country = models.ForeignKey('Country')
    districtid = models.IntegerField()
    name = models.CharField(max_length=40)
    
    class Meta:
        verbose_name = 'district'
        verbose_name_plural = 'districts'
        unique_together = ('country', 'districtid')

    def __unicode__(self):
        return self.name

