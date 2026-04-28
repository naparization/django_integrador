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

def carrinhos(request):
    carrinho = Carrinho.objects.all()
    return render(request, 'core/carrinho.html', {'carrinho': carrinho})

from django.shortcuts import redirect, get_object_or_404
from django.db import transaction

def finalizar_compra(request):
    if request.method == "POST":

        # limpa só o carrinho do usuário
        carrinho = Carrinho.objects.all()
        for item in carrinho:
            album = Album.objects.get(id=item.album_id)
            album.quantidade = album.quantidade - 1
            if (album.quantidade < 1):
                album.quantidade = 0
            album.save()
        Carrinho.objects.all().delete()
        
    return redirect('home')
