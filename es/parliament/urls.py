from django.conf.urls.defaults import patterns, url, include

from views import ESParlamentaryView

urlpatterns = patterns('meps.views',
    url(r'^deputy/(?P<pk>\w+)/$', ESParlamentaryView.as_view(), name='mep'),
)
