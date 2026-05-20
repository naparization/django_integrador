from django.db import models

# Create your models here.

class Artista(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(this):
        return(f'{this.nome}')

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    valor = models.FloatField(default=0.0)
    quantidade = models.IntegerField(null=False, default = 0)

    def __str__(this):
        return(f"{this.titulo} {this.valor}")
    
class Carrinho(models.Model):
    album = models.ForeignKey(Album, default=1, on_delete=models.CASCADE)
    usuario_id = models.IntegerField(null=False, default=1)

class Livro(models.Model):
    titulo = models.CharField(max_length=100),
    autor = models.ForeignKey(Artista, on_delete=models.CASCADE),
    ano = models.IntegerField(null=False, default=0)

class Emprestimo_Livro(models.Model):
    livro_id = models.ForeignKey(Livro, on_delete=models.CASCADE),
    pessoa = models.CharField(max_length=100),
    data_devolucao = models.DateField(),
    

        
        