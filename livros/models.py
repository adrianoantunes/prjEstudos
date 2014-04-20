from django.db import models

# Create your models here.
class Livro(models.Model):
	nome = models.CharField(max_length='50', blank=False, null=False)
	editora = models.CharField(max_length='50', blank=False, null=False)
	escritor = models.CharField(max_length='50', blank=False, null=False)
	