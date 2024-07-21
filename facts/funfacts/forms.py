from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
class AddSongForm(forms.ModelForm):
	title = forms.CharField(label = 'Название', widget = forms.TextInput(attrs={'class': 'form-input'}))
	content = forms.CharField(label = 'Содержание', widget = forms.Textarea(attrs={'class': 'form-input'}))

	def __init__(self,*args,**kwargs):
		super().__init__(*args, **kwargs)
		self.fields['author'].empty_label= "Author has not been choosen"



	class Meta:
		model = Song
		fields =['title', 'author', 'content', 'cat', 'Image']
class AddAuthorForm(forms.ModelForm):
	name = forms.CharField(label = "Имя автора")
	class Meta:
		model = Author
		fields = ['name',]
	def __init__(self,*args,**kwargs):
		super().__init__(*args, **kwargs)

class AddCategoryForm(forms.ModelForm):
	name =  forms.CharField(label = "Добавить категорию")
	class Meta:
		model = Category
		fields = ['name',]
		


class RegisterUserForm(UserCreationForm):
	username = forms.CharField(label = 'Юзернейм', widget = forms.TextInput(attrs ={'class':'form-input'}))
	email = forms.EmailField(label = 'Почта', widget=forms.EmailInput(attrs={'class':'form-input'}))
	password1 = forms.CharField(label = 'Твой секретный ключик', widget = forms.PasswordInput(attrs={'class':'form-input'}))
	password2 = forms.CharField(label = 'Повтори', widget = forms.PasswordInput(attrs={'class':'form-input'}))

	class Meta:
		model =User
		fields = ('username','email', 'password1', 'password2',)


class LoginUserForm(AuthenticationForm):
	username = forms.CharField(label = 'Юзернейм', widget = forms.TextInput(attrs ={'class':'form-input'}))
	password = forms.CharField(label = 'Секретный ключик', widget = forms.PasswordInput(attrs={'class':'form-input'}))
class AddUrlForm(forms.Form):
	url = forms.CharField(label = 'URL', widget = forms.URLInput(attrs = {'class':"form-input"}))

	class Meta:
		fields = '__all__'