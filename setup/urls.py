from django.contrib import admin
from django.urls import path
from core.views import home, adicionar_ao_carrinho, carrinhos, finalizar_compra, editar_album, novo_album, excluir_album, novo_artista, listar_artistas


urlpatterns = [
    path('carrinho/', carrinhos, name='carrinho' ),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('adicionar/carrinho/<str:id>', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('finalizar_compra/', finalizar_compra, name='finalizar_compra'),
    path('editar/<int:id>/', editar_album, name='editar_album'),
    path('novo_disco/', novo_album, name='novo_album'),
    path('novo_artista/', novo_artista, name='novo_artista'),
    path('excluir/album/<str:id>', excluir_album, name='excluir_album'),
    path('listar_artistas/', listar_artistas, name='listar_artistas'),
]
