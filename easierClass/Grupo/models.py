from django.db import models
from ..Usuario.models import *
from ..Sala.models import *


class Grupo(models.Model):
    sala = models.ForeignKey(Sala, on_delete = models.CASCADE)
    alunos = models.ManyToManyField(Aluno)