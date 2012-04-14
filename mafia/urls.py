from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'mafia.views.login'),
    url(r'^games/', include('mafia.games.urls')),
)
