from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from enderecos.api.serializers import EnderecosSerializer


class EnderecosViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecosSerializer
