from django.db import models


class Conquista(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=50)