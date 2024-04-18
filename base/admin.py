from django.contrib import admin
from .models import Material, Comanda, RaportCalitate
from import_export.admin import ImportExportModelAdmin


class MaterialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class ComandaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class RaportCalitateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
# Register your models here.
admin.site.register(Material, MaterialAdmin)
admin.site.register(Comanda,ComandaAdmin)
admin.site.register(RaportCalitate,RaportCalitateAdmin)
