from django.contrib import admin
from .models import Documento
from import_export.admin import ImportExportModelAdmin

@admin.register(Documento)
class DocumentoAdmin(ImportExportModelAdmin):
    list_display= ( 'pertence', 'descricao')
