from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import RegistroHoraExtra


@admin.register(RegistroHoraExtra)
class HoraExtraAdmin(ImportExportModelAdmin):
    list_display = ('funcionario', 'motivo', 'horas')
    list_editable = ('horas',)
