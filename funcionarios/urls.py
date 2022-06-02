from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
                    FuncionariosList, 
                    FuncionariosEdit, 
                    FuncionariosDelete, 
                    FuncionariosCreate, 
                    )

from .views_2.import_export import export_data, import_data

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionariosEdit.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/', FuncionariosDelete.as_view(), name='delete_funcionario'),
    path('cadastrar-funcionario/', FuncionariosCreate.as_view(), name='create_funcionario'),

    path('export/', export_data, name='export_data'),
    path('import/', import_data, name='import_data'),
]

# Para carregar STATIC e as MIDIAS
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)