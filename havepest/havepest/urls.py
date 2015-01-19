from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'havepest.views.index'),
    url(r'^contact/$', 'havepest.views.contact'),
    url(r'^photos/', include('photos.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
