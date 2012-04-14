from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Manage session
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^register/$', register_page),
    (r'^register/success/$', direct_to_template,
       {'template': 'registration/register_success.html'}),

    url(r'^login/$', 'mafia.views.login'),
    url(r'^games/', include('mafia.games.urls')),
    url(r'^index/index', 'mafia.index.views.index')
)
