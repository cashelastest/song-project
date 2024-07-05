from django.urls import path
from . import views

urlpatterns = [
path('', views.SongHome.as_view(), name = 'home'),
path('category/<int:cat_id>/', views.category, name = 'category'),
path('login/', views.LoginUser.as_view(), name = 'login'),
path('registration/', views.RegisterUser.as_view(), name = 'registration'),
path('song/<slug:song_slug>/', views.Show_Song.as_view(), name= "song"),
path('songs/genres/<int:cat_id>/', views.menu, name = 'menu'),
path('songs/authors/<slug:author_slug>/', views.Choose_Author.as_view(), name="choose_author"),
path('songs/authors/', views.authorPage, name = "authorsPage"),
path('forms/', views.addSong.as_view(), name = "addSong"),
path('logout/', views.logout_user, name = 'logout'),
path('songs/addAuthor/', views.addAuthor.as_view(), name = 'addAuthor'),
path('songs/addCategory/', views.addCategory.as_view(), name = 'addCategory'),


]