from django.db import models
from django.contrib.auth.models import AbstractUser

""" 
class Ciclista(models.Model):
    cpf = models.CharField('CPF', primary_key = True)
    nome = models.CharField('Nome', max_length=255)
    data_nascimento = models.DateField('Data de nascimento')
    grupo = models.CharField('Grupo', max_length=200)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=2)
    email = models.EmailField('E-mail', max_length=255)
    telefone = models.CharField('Telefone', max_length=14)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

"""
class Ciclista(AbstractUser):
    nome = models.CharField('Nome completo', max_length=255)
    cpf = models.CharField('CPF', unique=True)
    data_nascimento = models.DateField('Data de nascimento')
    grupo = models.CharField('Grupo', max_length=200)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=2)
    telefone = models.CharField('Telefone', max_length=14)

    email = models.EmailField('E-mail', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'cpf']

    def __str__(self):
        return f"{self.nome} ({self.email})"


class TipoEvento(models.Model):
    descricao = models.CharField('Descrição', max_length=100)

    def __str__(self):
        return self.descricao

class Evento(models.Model):
    nome_evento = models.CharField('Nome do evento', max_length=255)
    valor_inscricao = models.DecimalField('Valor da inscrição', max_digits=8, decimal_places=2)
    data_evento = models.DateField('Data do evento', db_index=True)
    data_inicio_inscricao = models.DateField('Data início inscrição')
    data_fim_inscricao = models.DateField('Data fim inscrição')
    distancia = models.FloatField('Distância')
    tipoEvento = models.ForeignKey(TipoEvento, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_evento

    class Meta:
        indexes = [models.Index(fields=['data_evento'])]

class Inscricao(models.Model):
    STATUS_CHOICES = [
        ('Pago', 'Pago'),
        ('Pendente', 'Pendente'),
        ('Cancelada', 'Cancelada'),
    ]
    data_inscricao = models.DateField('Data da inscrição', auto_now_add=True)
    forma_pagamento = models.CharField('Forma de pagamento', max_length=50)
    status = models.CharField('Status', max_length=45, choices=STATUS_CHOICES, default='Pendente')
    ciclista = models.ForeignKey(Ciclista, on_delete=models.PROTECT)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.ciclista} -> {self.evento} ({self.status})"