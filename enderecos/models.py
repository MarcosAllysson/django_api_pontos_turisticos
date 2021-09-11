from django.db import models


class Endereco(models.Model):
    linha_um = models.CharField(max_length=150)
    linha_dois = models.CharField(max_length=150, null=True, blank=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.linha_um}, {self.linha_dois}'

    class Meta:
        verbose_name = 'endereço'
        verbose_name_plural = 'endereços'
