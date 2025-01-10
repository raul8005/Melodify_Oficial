from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Album, Song, Comment, Message
from .forms import AlbumForm, SongForm, CommentForm, MessageForm

@login_required
def create_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.musician = request.user
            album.save()
            return redirect('musico:album_list')
    else:
        form = AlbumForm()
    return render(request, 'musico/crear_album.html', {'form': form})

@login_required
def upload_music(request):
    if request.method == "POST":
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('musico:song_list')
    else:
        form = SongForm()
    return render(request, 'musico/upload_music.html', {'form': form})

@login_required
def song_list(request):
    songs = Song.objects.filter(album__musician=request.user)
    return render(request, 'musico/song_list.html', {'songs': songs})

@login_required
def add_comment(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.song = song
            comment.save()
            return redirect('musico:song_list')  # Redirige a la lista de canciones
    else:
        form = CommentForm()
    return render(request, 'musico/add_comment.html', {'form': form, 'song': song})

@login_required
def album_list(request):
    albums = Album.objects.filter(musician=request.user)
    return render(request, 'musico/album_list.html', {'albums': albums})

@login_required
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('musico:message_list')
    else:
        form = MessageForm()
    return render(request, 'musico/send_message.html', {'form': form})

@login_required
def message_list(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'musico/message_list.html', {'messages': messages})









