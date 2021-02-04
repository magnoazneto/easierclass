from django.db import models


class Instituicao(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=6)
    criado_em = models.DateField(auto_now_add=True)