from django.db import models
from ..Instituicao.models import *
from ..Usuario.models import *


class Sala(models.Model):
    instituicao = models.ForeignKey(Instituicao)
    nome = models.CharField(max_length=20)
    criado_em = models.DateField(auto_now_add=True)
    max_alunos = models.IntegerField()
    '''
    criado_por = models.ForeignKey(
        'Professor',
        related_name='atividade',
        on_delete=models.CASCADE
    )
    '''


class Inscricao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    data_inscricao = models.DateField(auto_now_add=True)