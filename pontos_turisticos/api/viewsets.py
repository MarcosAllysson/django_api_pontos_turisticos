from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from pontos_turisticos.models import PontoTuristico
from pontos_turisticos.api.serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'descricao', 'endereco__linha_um']
    permission_classes = (IsAuthenticated,)
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    # def get_queryset(self):
    #     return PontoTuristico.objects.filter(aprovado=True)

    # GET
    # def list(self, request, *args, **kwargs):
    #     pass

    # POST
    # def create(self, request, *args, **kwargs):
    # pass
    # SOBSCREVENDO MÉTODO SUPER CLASSE
    # return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    # DELETE
    # def destroy(self, request, *args, **kwargs):
    #     pass

    # GET
    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # PUT
    # def update(self, request, *args, **kwargs):
    #     pass

    # PATCH
    # def partial_update(self, request, *args, **kwargs):
    #     pass

    # PERSONALIZADA
    @action(methods=['GET'], detail=True)
    def denunciar(self, request, pk=None):
        pass
