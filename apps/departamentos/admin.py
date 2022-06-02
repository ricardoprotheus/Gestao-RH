from django.contrib import admin
from .models import Departamento
from import_export.admin import ImportExportModelAdmin



@admin.register(Departamento)
class DepartamentoAdmin(ImportExportModelAdmin):
    list_display = ('departamento', 'empresa')

