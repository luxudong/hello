# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^quote/$', views.QuoteView.as_view()),
	url(r'^document/$', views.DocumentView.as_view()),
	url(r'^list/$', 'market.views.list',name='list'),
)
