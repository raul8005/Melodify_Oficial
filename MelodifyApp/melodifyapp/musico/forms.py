from django import forms
from .models import Album, Song, Comment, Message

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'cover_image', 'release_date']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'duration', 'file']
        widgets = {
            'duration': forms.NumberInput(attrs={'min': 0}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tu comentario aquí...'}),
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['recipient', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tu mensaje aquí...'}),
        }

