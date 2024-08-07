from django.db import models
from django.urls import reverse
from slugify import slugify
from unidecode import unidecode

class Fact(models.Model):
	title = models.CharField(max_length = 255, help_text = 'Enter title')
	content = models.TextField(blank = True)
	Image = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
	date = models.DateField(auto_now = True)
	def __str__(self):
		return self.title


class Author(models.Model):
	name = models.CharField(max_length = 255)
	slug= models.SlugField(max_length=255,db_index = True, unique = True)
	def __str__(self):
		return self.name
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.name))
		super().save(*args, **kwargs)
	def get_absolute_url(self):
		return reverse('author', kwargs={'author_slug': self.slug})

class Category(models.Model):
	name = models.CharField(max_length = 255, db_index = True)
	slug = models.SlugField(max_length=255, db_index = True, null = True)
	def save(self, *args,**kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.name), allow_unicode=True)
		super().save(*args,**kwargs)

	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('category', kwargs={'cat_slug': self.slug})
	def get_absolute_pk(self):
		return self.pk

class Song(models.Model):
	title = models.CharField(max_length = 255, verbose_name="Название")
	slug = models.SlugField(max_length=255, unique=True, db_index = True, verbose_name = "URL")
	author = models.ForeignKey('Author', on_delete = models.PROTECT, null = True,verbose_name='Автор', blank = True)
	content = models.TextField(verbose_name="Содержание")
	Image = models.ImageField(upload_to = 'photos/%Y/%m/%d/', verbose_name="Фото")
	Video = models.FileField(upload_to = 'files/', verbose_name = 'файл', blank = True, null = True)
	cat = models.ManyToManyField(Category, verbose_name='Жанры (Можешь выбрать несколько, разраб постарался)',related_name='category')

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.title), allow_unicode=True)
		super().save(*args, **kwargs)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('song', kwargs={'song_slug': self.slug})

	def get_absolute_url_author(self):
		return reverse('author', kwargs={'author_slug': self.author.slug})

	def get_absolute_url_cat(self):
		return reverse('category', kwargs = {'cat_slug':self.catS.slug})


