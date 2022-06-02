from django.contrib import admin
from .models import Empresa
from import_export.admin import ImportExportModelAdmin


@admin.register(Empresa)
class EmpresaAdmin(ImportExportModelAdmin):
    list_display = ('nome',)
