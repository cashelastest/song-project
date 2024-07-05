from .models import *

class DataMixin:
	paginate_by = 4
	def get_user_context(self, **kwargs):
		context = kwargs
		author = Author.objects.all()
		context['author']=author
		if 'author_selected' not in context:
			context['author_selected']=0
		return context