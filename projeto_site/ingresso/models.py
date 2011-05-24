from django.db import models
import eventos

# Create your models here.
class IngressoEsporte(models.Model):
    esporte =  models.OneToOneField(eventos.models.Esporte)
##    esporte =  models.ForeignKeyField(eventos.models.Esporte)
    descricao = models.TextField()
     
class IngressoShow(models.Model):
    show =  models.OneToOneField(eventos.models.Show)
    descricao = models.TextField()
class IngressoFilme(models.Model):
    filme =  models.OneToOneField(eventos.models.Filme)
##    esporte =  models.ForeignKeyField(eventos.models.Esporte)
    descricao = models.TextField()
class IngressoPeca(models.Model):
    peca =  models.OneToOneField(eventos.models.Peca)
##    esporte =  models.ForeignKeyField(eventos.models.Esporte)
    descricao = models.TextField()
