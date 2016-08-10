from django.contrib import admin
from .models import *

from django import forms
from django.forms import widgets
from django.forms.utils import flatatt
from django.utils.encoding import smart_unicode
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

class AccDescriptionInline(admin.TabularInline):
    model = AccDescription

class DistrictChoiceWidget(widgets.Select):
    def render(self, name, value, attrs=None, choices=()):
        self.choices = [(u"", u"---------")]
        if value is None:
            # if no district has been previously selected,
            # render either an empty list or, if a country has
            # been selected, render its districts
            value = ''
            accommodatie = self.form_instance.instance
            id = accommodatie.accid
            if id and accommodatie.country:
                for district in accommodatie.country.district_set.all():
                    self.choices.append((district.id, smart_unicode(district)))
        else:
            # if a district X has been selected,
            # render only these districts, that belong
            # to X's country
            district = District.objects.get(id=value)
            for distr in District.objects.filter(country=district.country):
                self.choices.append((distr.id, smart_unicode(distr)))

        # copy-paste from widgets.Select.render
        final_attrs = self.build_attrs(attrs, name=name)
        output = [u'<select%s>' % flatatt(final_attrs)]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append('</select>')
        return mark_safe(u'\n'.join(output))

class AccommodatieForm(forms.ModelForm):
    district = forms.ModelChoiceField(District.objects,
            widget=DistrictChoiceWidget(),
            label=_('District'), required=False)

    class Meta:
        model = Accommodatie
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        We need access to the country field in the district widget, so we
        have to associate the form instance with the widget.
        """
        super(AccommodatieForm, self).__init__(*args, **kwargs)
        self.fields['district'].widget.form_instance = self
        
class AccommodatieAdmin(admin.ModelAdmin):
    list_filter = (('country', admin.RelatedOnlyFieldListFilter),
                  )
    list_display = ('accid', 'address', 'zipcode', 'city', 'district', 'country')
    inlines = [
        AccDescriptionInline,
    ]    
    form = AccommodatieForm

    class Media:
        js = ('http://ajax.googleapis.com/ajax/libs/jquery/1.4.0/jquery.min.js',
                '/static/js/district2.js')

       
admin.site.register(Accommodatie, AccommodatieAdmin)
admin.site.register(AccommodatieBeheerder)
admin.site.register(AccDescription)
admin.site.register(AccommodatiePictures)
admin.site.register(RegionLinks)
admin.site.register(RegionText)
admin.site.register(Users)
admin.site.register(Country)
admin.site.register(District)
admin.site.register(Language)
admin.site.register(AccommodatieType)