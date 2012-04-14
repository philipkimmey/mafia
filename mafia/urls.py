from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from index.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Manage session
    (r'^$', index),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^register/$', register_page),
    (r'^register/success/$', direct_to_template,
       {'template': 'registration/register_success.html'}),

    #url(r'^games/', include('mafia.games.urls')),
    #url(r'^index/index', 'mafia.index.views.index')
)
