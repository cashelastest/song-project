from django import template
from funfacts.models import *

register = template.Library()


@register.simple_tag(name='getauthor')
def get_author():
	return Author.objects.all() 

@register.inclusion_tag('funfacts/list_authors.html')
def show_authors(sort=None, author_selected=0, category_selected=0):
	if not sort:
		authors = Author.objects.all()
		category = Category.objects.all()
	else:
		authors = Author.objects.order_by(sort)
		category = Category.objects.order_by(sort)


	return {"authors":authors, "author_selected":author_selected, "cats":category, "category_selected":category_selected}

@register.inclusion_tag('funfacts/list_songs.html')
def block_song(sort = None):
	if not sort:
		songs = Song.objects.all()
	else:
		songs = Song.objects.order_by(sort)
	return{'songs':songs,}