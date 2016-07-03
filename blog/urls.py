# coding: utf-8
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin_article'),
    url(r'', include('fengzi_blog.urls')),
	#url(r'^ueditor', include('DjangoUeditor.urls')),
]
