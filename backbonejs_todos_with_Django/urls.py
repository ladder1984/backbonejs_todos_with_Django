# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from mytodo.views import *

urlpatterns = patterns('',


    url(r'^admin/', include(admin.site.urls)),
    url(r'^todo/control/$', control_cr),
    url(r'^todo/control/(\d*)$', control_ud),
    url(r'^todos/$', get_all),
    url(r'^$', index),
)
