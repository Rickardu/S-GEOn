# -*- coding: cp1252 -*-
from django.db import models
import eventos
# Create your models here.
class Ambiente(models.Model):  
    descricao = models.TextField()
    capacidadeTotal=models.IntegerField()
    endereco = models.CharField(max_length=200)
    pontodeReferencia = models.CharField(max_length=200)
    evento_choices=(
     ("Peça",models.ForeignKey(eventos.models.Peca)),
     ("Esporte",models.ForeignKey(eventos.models.Esporte)),
     ("Show",models.ForeignKey(eventos.models.Show)),
     ("Filme",models.ForeignKey(eventos.models.Filme)),
     )
  
    evento = models.CharField(max_length=200,choices=evento_choices )
    
class CasaShowAmbiente(Ambiente):
     nome = models.CharField(max_length=200)
     
     
class ClubeAmbiente(Ambiente):
     nome = models.CharField(max_length=200)
     
class CinemaAmbiente(Ambiente):
    nome = models.CharField(max_length=200)
    
        
class TeatroAmbiente(Ambiente):
    nome = models.CharField(max_length=200)
     
                                    
class AuitorioAmbiente(Ambiente):
    nome = models.CharField(max_length=200)
    
class GinasioAmbiente(Ambiente):
    nome = models.CharField(max_length=200)
     
class EstadioAmbiente(Ambiente):
    nome = models.CharField(max_length=200)
     
