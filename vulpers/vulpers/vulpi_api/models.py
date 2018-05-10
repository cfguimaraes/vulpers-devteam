from django.db import models

class User(models.Model):
	username = models.CharField('Login', max_length=32)
	phone = models.CharField('Telefone', max_length=14)
	descricao = models.CharField('Descrição', max_length=14)
