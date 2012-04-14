from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^new/$', 'games.views.new'),
    url(r'^(\d+)/$', 'games.views.game', name="game"),
    #url(r'^(\d+)/votes/$', 'games.views.votes'),
)
