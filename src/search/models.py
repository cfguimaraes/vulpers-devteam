# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Profissional(models.Model):
    class meta:
        db_table = "profissionais"

    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    classificacao = models.CharField(max_length=len("cavaleiro jedi"))

    def __str__(self):
        return self.nome
