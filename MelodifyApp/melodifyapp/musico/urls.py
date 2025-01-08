from django.urls import path
from . import views

app_name = 'musico'

urlpatterns = [
    path('create-album/', views.create_album, name='create_album'),
    path('upload-music/', views.upload_music, name='upload_music'),
    path('songs/', views.song_list, name='song_list'),
    path('songs/<int:song_id>/comment/', views.add_comment, name='add_comment'),
    path('album-list/', views.album_list, name='album_list'),
]
