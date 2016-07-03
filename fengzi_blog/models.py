# coding: utf-8
from django.db import models
from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import User

class Article(models.Model):
	title = models.CharField(
		max_length=10, 
		unique=True,
		verbose_name='标题'
	)
	author = models.ForeignKey(
		User, 
		null=True, 
		blank=True, 
		verbose_name='用户'
	)
	content = UEditorField(
		width=1100, 
		height=300, 
		verbose_name='内容'
	)
	tag = models.CharField(
		max_length=50, 
		null=True, 
		blank=True, 
		verbose_name='标签'
	)
	views = models.IntegerField(
		default=0, 
		verbose_name='阅读'
	)
   	pubd = models.DateTimeField(
		'pubd', 
		auto_now_add=True
	)

	class Meta:
		ordering = ['-pubd']

	def __unicode__(self): 
		return self.title

class User(models.Model):
	username = models.CharField(
		max_length=20, 
		verbose_name='用户名'
	)
	password = models.CharField(
		max_length=30, 
		verbose_name='密码'
	)

	def __unicode__(self):
		return self.username
