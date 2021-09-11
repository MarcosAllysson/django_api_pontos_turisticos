from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from pontos_turisticos.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet
from enderecos.api.viewsets import EnderecosViewSet
from comentarios.api.viewsets import ComentarionsViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet

router = routers.DefaultRouter()
router.register('pontoturistico', PontoTuristicoViewSet)
router.register('atracoes', AtracoesViewSet)
router.register('enderecos', EnderecosViewSet)
router.register('comentarios', ComentarionsViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
