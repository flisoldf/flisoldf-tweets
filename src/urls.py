from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    # url(r'^$', 'src.views.home', name='home'),
    url(r'configuracoes/', include('configurations.urls',
                                   namespace='configurations')),
)
