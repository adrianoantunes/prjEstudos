from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prjEstudos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'pessoas/', include('pessoas.urlsPessoas')),
    url(r'livros/', include('livros.urlsLivros')),
    url(r'alugueis/', include('alugueis.urlsAlugueis')),
)
