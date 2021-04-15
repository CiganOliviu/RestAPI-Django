from django.contrib import admin
from .models import *

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'coordinates', 'postal_code')


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', )


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'capital', 'official_language')


class ExtremeSportAdmin(admin.ModelAdmin):
    list_display = ('name', 'period')


admin.site.register(Location, LocationAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(ExtremeSport, ExtremeSportAdmin)








