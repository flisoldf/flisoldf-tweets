from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('configurations.views',
    url(r'^$', 'list', name='list'),
    url(r'^novo/$', 'new', name='new'),
    url(r'^atualizar/(?P<hashtag>[-\d])/$', 'edit', name='edit'),
    url(r'^excluir/(?P<hashtag>[-\d])/$', 'delete', name='delete'),
)
