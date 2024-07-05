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
		cats = Category.objects.all()
	else:
		authors = Author.objects.order_by(sort)
		cats = Category.objects.order_by(sort)

	return {"authors":authors, "author_selected":author_selected, "cats":cats, "category_selected":category_selected}