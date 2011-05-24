from django.db import models

# Create your models here.

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    dataEvento = models.DateTimeField()
    dataInclusao = models.DateTimeField()
    sinopse = models.TextField()
    def __unicode__(self):
        return self.nome
    
##    filme = ForeignKeyField(Filme)
##    esporte = ForeignKeyField(Esporte)
##    peca = ForeignKeyField(Peca)
##    show = ForeignKeyField(Show)
class Esporte(Evento):    
    equipeA=models.CharField(max_length=200)
    equipeB=models.CharField(max_length=200)
    
     
class Filme(Evento):    
    censura=models.IntegerField()
    estrela=models.CharField(max_length=200)
    genero=models.CharField(max_length=200)
     
class Peca(Evento):   
    companhia=models.CharField(max_length=200)
    genero=models.CharField(max_length=200)
     
class Show(Evento):
    artista=models.CharField(max_length=200)
    estilo=models.CharField(max_length=200)

##class Ingresso(models.Model):
##    ingresso =  models.OneToOneField( Esporte)
##    descricao = models.TextField()
