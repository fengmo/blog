# coding: utf-8
from django import forms
from django.forms import ModelForm
from models import Article, User

class ArticleForm(ModelForm):

	class Meta:
		model = Article
		exclude = ['views']

class LoginForm(ModelForm):
	password = forms.CharField(
		label=u'密码', 
		widget=forms.PasswordInput
	)

	class Meta:
		model = User
		exclude = []
