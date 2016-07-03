# coding: utf-8
from django.core.paginator import (
	Paginator, 
	EmptyPage, 
	PageNotAnInteger
)
from django.views.generic.edit import (
	CreateView, 
	UpdateView, 
	FormView
)
from django.views.generic import (
	ListView, 
	DetailView, 
	TemplateView
)
from django.contrib.auth import (
	authenticate, 
	login, logout
)
from django.http import HttpResponseRedirect
from forms import LoginForm, ArticleForm
from django.shortcuts import render
from django.http import Http404
from models import Article

class IndexView(ListView):
	template_name = 'index.html'
	context_object_name = 'article_list'

	def get_queryset(self, **kwargs):
		article_list = Article.objects.all().order_by('-pubd')
		paginator = Paginator(article_list, 5)
		page = self.request.GET.get('page')
		try:
			article_list = paginator.page(page)
		except PageNotAnInteger:
			article_list = paginator.page(1)
		except EmptyPage:
			artciel_list = paginator.page(paginator.num_pages)
		except Exception:
			raise Http404('页面不存在')
		return article_list

class  ADetailView(DetailView):
	template_name = 'article.html'
	context_object_name = 'article'

	def get_object(self, **kwargs):
		pk = self.kwargs.get('pk')
		try:
			article = Article.objects.get(pk=pk)
			article.views += 1
			article.save()
		except Article.DoesNotExist:
			raise Http404('文章不存在')
		return article

class ArchiveView(TemplateView):
	template_name = 'archive.html'
	
	def get_context_data(self, **kwargs):
		context = super(ArchiveView, self).get_context_data(**kwargs)
		context['archive_list'] = Article.objects.all()
		return context

class InfoView(TemplateView):
	template_name = 'info.html'

	def get_context_data(self, **kwargs):
		context = super(InfoView, self).get_context_data(**kwargs)
		context['QQ_info'] = '1220751818'
		context['email_info'] = ('xiaohadoop@gmail.com  1220751818@qq.com')
		return context

class APublishView(CreateView):
	form_class = ArticleForm
	success_url = '/'
	template_name = 'publish.html'

class AUpdateView(UpdateView):
	form_class = ArticleForm
	model = Article
	success_url = '/'
	template_name = 'update.html'

def blog_login(request):
	try:
		if request.method == 'POST':
			login_form = LoginForm(request.POST)
			if login_form.is_valid():
				username = login_form.cleaned_data['username']
				password = login_form.cleaned_data['password']
				user = authenticate(username=username, password=password)
				if user is not None and user.is_active:
					login(request, user)
					return HttpResponseRedirect('/')
				else:
					return render(request, 
						'fail.html', {'login_form': '账号或密码错误'}
					)
			else:
				return render(request, 
					'fail.html', {'login_form': '账号和密码不能为空'}
				)

		if request.method == 'GET':
			if request.user.is_authenticated():
				return HttpResponseRedirect('/')
			else:
				login_form = LoginForm()

	except Exception as e:
		raise Http404('方法错误')
	return render(request, 
		'login.html', {'login_form': login_form}
	)

def blog_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

