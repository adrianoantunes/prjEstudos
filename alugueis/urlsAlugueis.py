from django.conf.urls import patterns, include, url

urlpatterns = patterns('alugueis.views',
    url(r'^adicionar/$', 'aluguelAdicionar'),
    url(r'^editar/(?P<pk>\d+)/$', 'aluguelEditar'),
    url(r'^salvar/$', 'aluguelSalvar'),
    url(r'^pesquisar/$', 'aluguelPesquisar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'aluguelExcluir'),
    url(r'^$', 'aluguelListar'),
)
