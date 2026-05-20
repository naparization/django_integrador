from .models import Album, Artista
from django import forms

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo', 'artista', 'valor', 'quantidade']

        labels = {
            'titulo': 'Título',
            'artista': 'Artista',
            'valor': 'Valor',
            'quantidade': 'Quantidade'
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título do álbum'}),
            'artista': forms.Select(attrs={'placeholder': 'Artista do álbum'}),
            'valor': forms.NumberInput(attrs={'placeholder': 'Valor do álbum'}),
            'quantidade': forms.NumberInput(attrs={'placeholder': 'Quantidade do álbum'})
        }

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nome']

        labels = {
            'nome': 'Nome do Artista'
        }

        widgets = {
           'nome': forms.TextInput(attrs={'placeholder': 'Nome do artista'}), 
        }