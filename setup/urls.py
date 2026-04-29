from django.contrib import admin
from django.urls import path
from core.views import home, adicionar_ao_carrinho, carrinhos, finalizar_compra, editar_album


urlpatterns = [
    path('carrinho/', carrinhos, name='carrinho' ),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('adicionar/carrinho/<str:id>', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('finalizar_compra/', finalizar_compra, name='finalizar_compra'),
    path('editar/<int:id>/', editar_album, name='editar_album')
]
