from django.shortcuts import render, redirect, get_object_or_404
from musico.models import Song, Album, User
from .forms import SearchForm

def search_artist(request):
    results = []
    query = request.GET.get('query', '').strip()  # Asegúrate de manejar valores vacíos o espacios

    if query:
        # Busca canciones asociadas a músicos cuyo username coincida parcialmente
        results = Song.objects.filter(album__musician__username__icontains=query)

    return render(request, 'oyente/buscar_artista.html', {
        'form': SearchForm(),
        'results': results,
        'query': query,
    })

def comment_song(request, song_id):
    from musico.models import Comment, Song  # Evitar dependencias cruzadas innecesarias
    from musico.forms import CommentForm

    song = Song.objects.get(id=song_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.song = song
            comment.save()
            return redirect('oyente:search_artist')
    else:
        form = CommentForm()

    return render(request, 'oyente/comentar_cancion.html', {'form': form, 'song': song})
