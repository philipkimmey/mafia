from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^new/$', 'mafia.games.views.new'),
    url(r'^(\d+)/$', 'mafia.games.views.game'),
    url(r'^(\d+)/votes/$', 'mafia.games.views.votes'),
)