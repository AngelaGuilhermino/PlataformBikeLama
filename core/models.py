from django.db import models

class Ciclista(models.Model):
    cpf = models.CharField('CPF', primary_key = True)
    nome = models.CharField('Nome', max_length=255)
    data_nascimento = models.DateField('Data de nascimento')
    grupo = models.CharField('Grupo', max_length=200)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=2)
    email = models.EmailField('E-mail', max_length=255)
    telefone = models.CharField('Telefone', max_length=14)

class TipoEvento(models.Model):
    descricao = models.CharField('Descrição', max_length=100)

class Evento(models.Model):
    nome_evento = models.CharField('Nome_evento', max_length=255)
    valor_inscrição = models.DecimalField('Valor da inscrição', max_digits=8, decimal_places=2)
    data_evento = models.DateField('Data do evento')
    data_inicio_inscricao = models.DateField('Data início inscrição')
    data_fim_inscricao = models.DateField('Data fim inscrição')
    distancia = models.FloatField('Distância')
    tipoEvento = models.ForeignKey(TipoEvento, on_delete=models.PROTECT)


class Inscricao(models.Model):
    STATUS_CHOICES = [
        ('Pago', 'Pago'),
        ('Pendente', 'Pendente'),
        ('Cancelada', 'Cancelada'),
    ]
    data_inscricao = models.DateField('Data da inscrição')
    forma_pagamento = models.CharField('Forma de pagamento', max_length=50)
    status = models.CharField('Status', max_length=45, choices=STATUS_CHOICES)
    ciclista = models.ForeignKey(Ciclista, on_delete=models.PROTECT)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)