from django.conf.urls import patterns, include, url
from sousaie.blog.models import *
from sousaie.blog.views import *
from sousaie.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sousaie.views.home', name='home'),
    # url(r'^sousaie/', include('sousaie.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^sousaie/blog/$',list_blogs),
    (r'^sousaie/blog/(\d+)/$',view_blog_detail),               
)
