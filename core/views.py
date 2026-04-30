from django.shortcuts import redirect, render, get_object_or_404
from core.models import Album, Artista, Carrinho
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    listaAlbuns = Album.objects.all()
    return render(request, 'core/home.html', {'albuns': listaAlbuns})


def adicionar_ao_carrinho(request, id):
    album = Album.objects.get(id=id)
    Carrinho.objects.create(album=album)

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

@login_required
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

@login_required
def novo_album(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        valor = request.POST.get('valor')
        artista = request.POST.get('artista')
        quantidade = request.POST.get('quantidade')

        Album.objects.create(titulo = titulo, valor = valor, quantidade = quantidade, artista_id = artista)
        return redirect('home')
    
    return render(request, 'core/novo_album.html')

def excluir_album(request, id):
    album = Album.objects.get(id=id)
    album.delete()

    return redirect('home')

@login_required
def novo_artista(request):
    if request.method == "POST":
        titulo = request.POST.get('nome')

        Artista.objects.create(nome = titulo)
        return redirect('home')
    
    return render(request, 'core/novo_artista.html')

@login_required
def listar_artistas(request):
    Artistas = Artista.objects.all()
    return render(request, 'core/listar_artistas.html', {'artistas': Artistas})