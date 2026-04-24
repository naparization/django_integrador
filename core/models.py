from django.db import models

# Create your models here.

class Artista(models.Model):
    nome = models.CharField(max_length=100)

class Album(models.Model):
    titulo = models.CharField(max_length=100)
    artista_id = models.ForeignKey(Artista, on_delete=models.CASCADE)