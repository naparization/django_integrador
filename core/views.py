from django.shortcuts import redirect, render, get_object_or_404
from core.models import Album, Carrinho

# Create your views here.

def home(request):
    listaAlbuns = Album.objects.all()
    return render(request, 'core/home.html', {'albuns': listaAlbuns})


def adicionar_ao_carrinho(request, id):
    album = Album.objects.get(id=id)
    Carrinho.objects.create(album=album)

    return redirect('home')


def editar_album(request, id):
    album = get_object_or_404(Album, id=id)

    if request.method == 'POST':
        album.titulo = request.POST.get('titulo')
        album.valor = request.POST.get('valor')
        album.quantidade = request.POST.get('quantidade')

        album.save()

        return redirect('home')

    return render(request, 'core/editar_album.html', {
        'album': album
    })


    
    