# coding: utf-8
from views import (
	IndexView,   ADetailView, 
	ArchiveView, APublishView, 
	AUpdateView, InfoView,
	blog_login,  blog_logout,
)
from django.contrib.auth.decorators import login_required
from django.conf.urls import include, url

urlpatterns = [
	url(r'^$', 
		IndexView.as_view(), 
		name='article_index'
	),
	url(r'^article/(?P<pk>\S+)/$', 
		ADetailView.as_view(), 
		name='article_detail'
	),
	url(r'^archive/$', 
		ArchiveView.as_view(), 
		name='archive_list'
	),
	url(r'^info/$', 
		InfoView.as_view(),
		name='info'
	),
	url(r'^blog_login/$', 
		blog_login, 
		name='blog_login'
	),
	url(r'^blog_logout/$', 
		login_required(blog_logout, login_url='/'), 
		name='blog_logout'
	),
	url(r'^publish/$', 
		login_required(APublishView.as_view(), 
			login_url='/blog_login/'
		),
		name='article_publish'
	),
	url(r'^update/(?P<pk>\S+)/$', 
		login_required(AUpdateView.as_view(), 
			login_url='/blog_login/'
		), 
		name='article_update'
	),
]
