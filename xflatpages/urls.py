# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url


xflatpages_urls = patterns('',
    # catch all pattern, after all try to match flatpage
    url(r'^(?P<url>.*/)$', 'xflatpages.views.flatpage', name='flatpage'),
)
