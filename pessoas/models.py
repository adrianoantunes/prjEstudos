from django.db import models

# Create your models here.
class Pessoa(models.Model):
	nome = models.CharField(max_length=50, blank=False, null=False)
	email = models.EmailField( blank=False, null=False)