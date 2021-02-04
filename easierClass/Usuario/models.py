from Instituicao.models import Instituicao
from django.db import models
from ..Conquista.models import *


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    dt_nasc = models.DateField()
    institucao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    conquistas = models.ManyToManyField(Conquista)


class Aluno(Usuario):
    matricula = models.CharField()


class Professor(Usuario):
    matricula = models.CharField()