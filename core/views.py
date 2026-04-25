from django.shortcuts import redirect, render

from core.models import Album, Carrinho

# Create your views here.

def home(request):
    listaAlbuns = Album.objects.all()
    return render(request, 'core/home.html', {'albuns': listaAlbuns})

def adicionar_ao_carrinho(request, id):
    album = Album.objects.get(id=id)
    Carrinho.objects.create(album = album)
    
    
    return redirect('home')


    
    