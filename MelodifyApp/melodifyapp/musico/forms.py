from django import forms
from .models import Album, Song, Comment, Message

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'release_date']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'album', 'file', 'duration']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content']

