from django.db import models

# Create your models here.

class Curso(models.Model):
	nome = models.CharField("Nome", max_length=50)
	sigla = models.CharField("Sigla", max_length=5)
	etiqueta = models.SlugField("Etiqueta", max_length=50)
	
	def __str__(self):
		return self.nome
