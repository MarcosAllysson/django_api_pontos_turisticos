from django.db import models


class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_funcionamento = models.TextField()
    idade_minima = models.IntegerField()
    foto = models.ImageField(upload_to='atracoes', null=True, blank=True)
    observacoes = models.CharField(max_length=100, null=True, blank=True)

    def str(self):
        return self.nome

    class Meta:
        verbose_name = 'atração'
        verbose_name_plural = 'atrações'
