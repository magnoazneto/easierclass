from django.db import models
from ..Sala.models import *


class Atividade(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=100)
    criado_em = models.DateField(auto_now_add=True)
    data_entrega = models.DateField()
'''
    criado_por = models.ForeignKey(
        'Professor',
        related_name='atividade',
        on_delete=models.CASCADE
    )
'''


class Atribuicao(models.Model):
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    
    
class Entrega(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    resposta = models.TextField(max_length=250)
    url_resposta = models.URLField()
    data_entrega = models.DateField(auto_now_add=True)