from django.shortcuts import render
from django.db.models import Q
from pessoas.models import Pessoa
# Create your views here.

#chama a pag html index
def index(request):
	return render(request, 'index.html')

def pessoaAdicionar(request):
	return render(request, 'pessoas/formPessoas'.html)

def pessoaEditar(request):
	if request

def pessoaSalvar(request):


def pessoaPesquisar(request):


def pessoaExcluir(request):


def pessoaListar(request):