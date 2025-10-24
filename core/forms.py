from django import forms
from .models import Ciclista, Evento, Inscricao, TipoEvento

class CiclistaForm(forms.ModelForm):
    class Meta:
        model = Ciclista
        fields = ['nome', 'cpf', 'data_nascimento', 'grupo', 'cidade', 'estado', 'email', 'telefone']

class TipoEventoForm(forms.ModelForm): #adm
    class Meta:
        model = TipoEvento
        fields = ['descricao']

class EventoForm(forms.ModelForm): #adm
    class Meta:
        model = Evento
        fields = ['nome_evento', 'valor_inscricao', 'data_evento', 'data_inicio_inscricao', 'data_fim_inscricao', 'distancia', 'tipoEvento']

class InscricaoForm(forms.ModelForm): 
    class Meta: 
        model = Inscricao
        fields = ['forma_pagamento', 'evento']

