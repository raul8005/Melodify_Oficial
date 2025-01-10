from django.urls import path
from . import views

app_name = 'oyente'

urlpatterns = [
    path('buscar-artista/', views.search_artist, name='search_artist'),
    path('canciones/<int:song_id>/comentar/', views.comment_song, name='comment_song'),
]
