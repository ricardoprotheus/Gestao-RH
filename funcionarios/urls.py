
from django.urls import path, include
from .views import FuncionariosList
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
]

# Para carregar STATIC e as MIDIAS
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)