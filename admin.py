from django.contrib import admin

# Register your models here.

from .models import *

class AccommodatieAdmin(admin.ModelAdmin):
    list_filter = ('country', )

admin.site.register(Accommodatie, AccommodatieAdmin)
admin.site.register(AccommodatieBeheerder)
admin.site.register(AccDescription)
admin.site.register(AccommodatiePictures)
admin.site.register(RegionLinks)
admin.site.register(RegionText)
admin.site.register(Users)