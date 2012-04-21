from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('tweets.views',
    url('^$', 'list', name='list'),
    url(r'^list_ajax$', 'list_ajax', name='list_ajax'),
)
