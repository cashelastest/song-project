from .models import *


class DataMixin:
	paginate_by = 4
	def get_user_context(self, **kwargs):
		context = kwargs
		author = Author.objects.all()
		cats = Category.objects.all()
		context['author']=author
		context['cats'] = cats

		if 'author_selected' not in context:
			context['author_selected']=0
		elif 'category_selected' not in context:
			context['category_selected'] = 0
			
		return context