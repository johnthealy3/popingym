from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'gymfinder.views.map', name='map'),    
    url(r'^form/', 'gymfinder.views.loc', name='loc'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}),
    url(r'^singly/', include('singly.urls')),
    url(r'^feed/','gymfinder.views.get_fb_feed', name='feed'),
    url(r'^show_feed/','gymfinder.views.show_feed', name='show_feed'),
    # url(r'^popingym/', include('popingym.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
