from django.contrib import admin
from django.urls import include, path
from core.views import AlbumCadastroView, AlbumViewSet, ArtistaCadastroView, home, adicionar_ao_carrinho, carrinhos, finalizar_compra, editar_album, excluir_album, novo_artista, listar_artistas, excluir_item_carrinho
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'albums', AlbumViewSet, basename='album')

urlpatterns = [
    path('carrinho/', carrinhos, name='carrinho' ),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('adicionar/carrinho/<str:id>', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('finalizar_compra/', finalizar_compra, name='finalizar_compra'),
    path('editar/<int:id>/', editar_album, name='editar_album'),
    # path('novo_disco/', novo_album, name='novo_album'),
    path('novo_album/', AlbumCadastroView.as_view(), name='novo_album'),
    path('novo_artista_2/', ArtistaCadastroView.as_view(), name='novo_artista_2'),
    path('novo_disco/', listar_artistas, name='dispositivo_lista'),
    path('novo_artista/', novo_artista, name='novo_artista'),
    path('excluir/album/<str:id>', excluir_album, name='excluir_album'),
    path('excluir/item_carrinho/<str:id>', excluir_item_carrinho, name='excluir_item_carrinho'),
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api_token_auth'),


    path('listar_artistas/', listar_artistas, name='listar_artistas'),
]
