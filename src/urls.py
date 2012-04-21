from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'configuracoes/', include('configurations.urls',
                                   namespace='configurations')),

    url(r'', include('tweets.urls', namespace='tweets')),
)
