from django.urls import path
from . import views

urlpatterns = [
path('', views.SongHome.as_view(), name = 'home'),

path('login/', views.LoginUser.as_view(), name = 'login'),
path('registration/', views.RegisterUser.as_view(), name = 'registration'),
path('song/<slug:song_slug>/', views.Show_Song.as_view(), name= "song"),
path('songs/genres/<slug:cat_slug>/', views.Category.as_view(), name = 'category'),
path('songs/authors/<slug:author_slug>/', views.Choose_Author.as_view(), name="author"),
path('songs/authors/', views.authorPage, name = "authorsPage"),
path('forms/', views.addSong.as_view(), name = "addSong"),
path('logout/', views.logout_user, name = 'logout'),
path('songs/addAuthor/', views.addAuthor.as_view(), name = 'addAuthor'),
path('songs/addCategory/', views.addCategory.as_view(), name = 'addCategory'),
path('songs/download/', views.download, name = 'downloads'),
path('accounts/profile/', views.red, name = 'red'),


]