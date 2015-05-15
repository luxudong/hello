from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^website', views.WebsiteView.as_view()),
	url(r'^index', views.IndexView.index,name='index')
)