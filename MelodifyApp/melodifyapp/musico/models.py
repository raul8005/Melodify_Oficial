from django.db import models
from django.contrib.auth.models import User
from django.conf import settings  # Importa el modelo de usuario configurado

class Album(models.Model):
    title = models.CharField(max_length=100)
    musician = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="albums")
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    file = models.FileField(upload_to="musico/songs/")
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.user} en {self.song.title}"
