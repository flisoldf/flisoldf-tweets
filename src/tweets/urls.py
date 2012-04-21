from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('tweets.views',
    url('$', 'list', name='list'),
)
