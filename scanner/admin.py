from django.contrib import admin
from . import models

class BarangInline(admin.TabularInline):
    model = models.RencanaKirimDetail

class RencanaKirimAdmin(admin.ModelAdmin):
    inlines = [
        BarangInline,
    ]

admin.site.register(models.Barang)
admin.site.register(models.RencanaKirim,RencanaKirimAdmin)
admin.site.register(models.RencanaKirimDetail)

