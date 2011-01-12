from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('elearning.views',
    (r'^$', 'index'),
)
