from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


import requests

from .models import *
from .forms import *
from .utils import *



class SongHome(DataMixin,ListView):

	model = Song
	context_object_name = 'songs'
	template_name = 'funfacts/home.html'


	def get_context_data(self,*, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def=self.get_user_context(title="home", author_selected = 0)
		
		return dict(list(context.items())+list(c_def.items()))

def login(request):
	return render(request, 'funfacts/login.html', {'title': 'login'})
def registration(request):
	return render(request, "funfacts/registration.html", {'title': 'regisration'})



def songs(request):

	songs = Song.objects.all()
	context={'songs':songs, 'title':'SONGS'}
	return render(request, 'funfacts/songs.html', context=context)






def category (request, cat_slug):
	cats = Category.objects.all()
	songs = Song.objects.filter(cat__slug =cat_slug)
	context = {
	"cats": cats,
	'songs': songs,
	'title':'songs',
}
	return render(request, 'funfacts/home.html', context=context)

class Category(DataMixin,ListView):
	model = Song
	template_name = "funfacts/home.html"
	context_object_name= 'songs'
	allow_empty= True
	def get_queryset(self):

		return Song.objects.filter(cat__slug=self.kwargs['cat_slug'])

	def get_context_data(self,*, object_list = None, **kwargs):
		context = super().get_context_data(**kwargs)
		try:
			s = context['songs'][0]
			c_def = self.get_user_context(title = "Категории" + str(s.cats),
			category_selected = s.cat_id)

		except:
			c_def=self.get_user_context(title="home", category_selected = 0)

		return dict(list(context.items())+ list(c_def.items()))

class Choose_Author(DataMixin,ListView):
	model = Song
	template_name = "funfacts/home.html"
	context_object_name= 'songs'
	allow_empty= True
	def get_queryset(self):

		return Song.objects.filter(author__slug=self.kwargs['author_slug'])

	def get_context_data(self,*, object_list = None, **kwargs):
		context = super().get_context_data(**kwargs)
		try:
			s = context['songs'][0]
			c_def = self.get_user_context(title = "Категории" + str(s.author),
			author_selected = s.author_id)

		except:
			c_def=self.get_user_context(title="home", author_selected = 0)

		return dict(list(context.items())+ list(c_def.items()))



def authorPage(request):
	songs = Song.objects.all()

	context={'songs':songs, 'title':'SONGS'}
	return render(request, 'funfacts/songs.html', context=context)


class Show_Song(DataMixin,DetailView):
	model = Song
	template_name = 'funfacts/song.html'
	slug_url_kwarg = 'song_slug'
	context_object_name='song'
	def get_context_data(self, *, object_list=None, **kwargs):

		context = super().get_context_data(**kwargs)

		c_def = self.get_user_context()


		return dict(list(context.items())+list(c_def.items()))



class addSong(DataMixin, CreateView):
	form_class = AddSongForm
	template_name = 'funfacts/addSong.html'
	success_url = reverse_lazy('home')
	login_url = reverse_lazy('login')
	

	def get_context_data(self, *,object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title = 'AddPage')
		return dict(list(context.items())+list(c_def.items()))

class addAuthor(DataMixin, CreateView):
	form_class = AddAuthorForm
	template_name = 'funfacts/add_author.html'
	success_url = reverse_lazy('addSong')

	def get_context_data(self,*,object_list = None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title = 'Добавить автора')
		return dict(list(context.items())+list(c_def.items()))
class addCategory(DataMixin, CreateView):
	form_class = AddCategoryForm
	template_name = 'funfacts/add_category.html'
	success_url = reverse_lazy('addSong')

	def get_context_data(self,*,object_list = None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title = 'Добавить категорию')
		return dict(list(context.items())+list(c_def.items()))

class RegisterUser(DataMixin, CreateView):
	form_class = RegisterUserForm
	template_name = 'funfacts/registration.html'
	success_url = reverse_lazy('login')

	def get_context_data(self, *,object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def =  self.get_user_context(title = 'regist')
		return dict(list(context.items())+list(c_def.items()))


class LoginUser(DataMixin,LoginView):
	form_class=LoginUserForm
	template_name = 'funfacts/login.html'
	success_url = reverse_lazy('home')
	login_url = reverse_lazy('home')

	def get_context_data(self,*,object_list =None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title = 'Authorithation')
		return dict(list(context.items())+ list(c_def.items()))
def logout_user(request):
	logout(request)
	return redirect('home')
class addURL(DataMixin, CreateView):
	form_class = AddUrlForm
	template_name = 'funfacts/urls.html'

	def get_context_data(self,*, object_list =None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title = 'addURL')
		return dict(list(context.items())+ list(c_def.items()))

def download(request):
	if request.method == 'POST':
		form = AddUrlForm(request.POST)
		if form.is_valid():

			name = form.cleaned_data['name']
			url = form.cleaned_data['url']
			chunk_size = 512
			r = requests.get(url, stream = True)
			with open(f"{name}.mp4", 'wb') as f:

				f.write(r.content)
				f.close()


	else:

		form = AddUrlForm()
	context ={
	'title': 'downloads',
	'form': form,
	}
	return render(request, 'funfacts/download.html',context=context)
def red(request):
	return redirect('home')
