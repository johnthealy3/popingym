from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gymfinder.views.login', name='login'),   
    url(r'^map/', 'gymfinder.views.map', name='map'),    
    url(r'^form/', 'gymfinder.views.loc', name='loc'),
    url(r'^singly/', include('singly.urls')),
    # url(r'^popingym/', include('popingym.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
