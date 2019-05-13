from django.db import models

# Create your models here.

class Register(models.Model):
	nome = models.CharField("Nome", max_length=30)
	email = models.EmailField("Email", max_length=30)
	data_nascimento = models.DataField("Data_nascimento")
	celular = models.IntegerField("Celular", max_length=50)
	usuario = models.SlugField("Usuario", max_length=15)
	senha = models.SlugField("Senha", max_length=15)
	endereco = models.SlugField("Endereco", max_length=30)
	cidade = models.SlugField("Cidade", max_length=30)
	estado = models.SlugField("Estado", max_length=2)
	cep = models.SlugField("Cep", max_length=10)
	
	def __str__(self):
		return self.nome
