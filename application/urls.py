from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin-byz/', include(admin.site.urls)),
    
    url(r'^', include('website.urls')),
    
    url(r'^captcha/', include('captcha.urls')),
)

handler500 = 'website.views.root.server_error'
