from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carrinho/<int:id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('editar/<int:id>/', views.editar_album, name='editar_album'),
]
