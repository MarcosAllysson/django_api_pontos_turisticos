from rest_framework.serializers import HyperlinkedRelatedField
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from pontos_turisticos.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializer
from enderecos.api.serializers import EnderecosSerializer


class PontoTuristicoSerializer(ModelSerializer):
    # HyperLinked Related field
    # atracoes = HyperlinkedRelatedField(many=True, read_only=True, view_name='atracao-detail')

    # Nested Serializer
    atracoes = AtracoesSerializer(many=True)
    endereco = EnderecosSerializer()

    # Serializer Method field
    descricao_completa = SerializerMethodField()

    def get_descricao_completa(self, obj):
        # obj representa o objeto, instância do modelo em si.
        return f'{obj.nome}, {obj.descricao}'

    class Meta:
        model = PontoTuristico
        fields = (
            'id',
            'nome',
            'descricao',
            'aprovado',
            'atracoes',
            'comentarios',
            'avaliacoes',
            'endereco',
            'foto',
            'descricao_completa',
            'get_descricao_completa_dois',
        )
