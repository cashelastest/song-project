from django.contrib import admin
from .models import *
class SongAdmin(admin.ModelAdmin):
	list_display=('id', 'title','author', 'Image')
	list_display_links = ('id','title','Image')
	search_fields = ('title', 'content')
	list_editible = ('title','author')
	list_filter = ("author",)
	prepopulated_fields={"slug":('title',)}

class CategoryAdmin(admin.ModelAdmin):
	list_display=('id', 'name')
	list_display_links=('id', 'name')
	search_fields = ("name",)
	prepopulated_fields={"slug":('name',)}

class AuthorAdmin(admin.ModelAdmin):
	list_display= ('id', 'name')
	list_display_links = ('id', 'name')
	search_fields = ('name',)
	prepopulated_fields={"slug":('name',)}

admin.site.register(Song, SongAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
# Register your models here.
