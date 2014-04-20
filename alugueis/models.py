from django.db import models
from pessoas.models import Pessoa
from livros.models import Livro

# Create your models here.
class Aluguel(models.Model):
	pessoa = models.ForeignKey(Pessoa)
	livro = models.ForeignKey(Livro)