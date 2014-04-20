from django.conf.urls import patterns, include, url

urlpatterns = patterns('livros.views',
    url(r'^adicionar/$', 'livroAdicionar'),
    url(r'^editar/(?P<pk>\d+)/$', 'livroEditar'),
    url(r'^salvar/$', 'livroSalvar'),
    url(r'^pesquisar/$', 'livroPesquisar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'livroExcluir'),
    url(r'^$', 'livroListar'),
)