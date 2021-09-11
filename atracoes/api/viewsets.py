from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from atracoes.api.serializers import AtracoesSerializer


class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer
    filterset_fields = ['nome', 'descricao']
