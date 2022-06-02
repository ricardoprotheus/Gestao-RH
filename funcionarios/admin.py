from django.contrib import admin
from .models import Funcionario
from import_export.admin import ImportExportModelAdmin


@admin.register(Funcionario)
class FuncionarioAdmin(ImportExportModelAdmin):
    list_display = ('nome', 'telefone',  'empresa')
    list_editable = ('empresa',)
