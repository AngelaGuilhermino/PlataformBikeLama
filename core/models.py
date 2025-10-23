from django.db import models

# Create your models here.

class ciclista(models.Model):
    nome = models.CharField('Nome', max_length=50)
    data = models.DateField('Data')
    cpf = models.IntegerField('CPF', primary_key = True)
    grupo = models.CharField('Nome', max_length=25)
    cidade = models.CharField('Cidade', max_length=25)
    estado = models.CharField('Estado', max_length=25)
    email = models.models.TextField('E-mail', max_length=50)
    telefone = models.IntegerField('Telefone')

class TipoEvento(models.Model):
    descricao = models.TextField('Descrição')

class Evento(models.Model):
    nome_evento = models.CharField('Nome_evento', max_length=50)
    valor_inscrição = models.IntegerField('Valor_inscrição')
    data_evento = models.DateField('Data_evento')
    data_inicio_inscricao = models.DateField('Data_inicio_inscricao')
    data_fim_inscricao = models.DateField('Data_fim_inscricao')
    distancia = models.FloatField('Distancia')


class Inscricao(models.Model):
    idInscricao = models.AutoField(primary_key=True)
    data_inscricao = models.DateField('Data_inscricao')
    forma_pagamento = models.CharField('Forma_pagamento', max_length=50)
    status = models.CharField('Status', max_length=25)