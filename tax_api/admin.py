from django.contrib import admin

from tax_api.models import TaxObject

class TaxObjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_display_links = ['name']

admin.site.register(TaxObject, TaxObjectAdmin)
