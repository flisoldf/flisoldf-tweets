from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('configurations.views',
    url(r'$', 'list', name='list'),
)
