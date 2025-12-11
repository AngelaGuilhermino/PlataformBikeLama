from django import forms
from .models import Ciclista, Evento, Inscricao, TipoEvento

class CiclistaForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    senha2 = forms.CharField(label="Confirme a senha", widget=forms.PasswordInput)

    class Meta:
        model = Ciclista
        fields = ['nome', 'username', 'cpf', 'data_nascimento', 'grupo', 'cidade', 'estado', 'email', 'telefone']

    def clean(self):
        cleaned_data = super().clean()
        s1 = cleaned_data.get("senha")
        s2 = cleaned_data.get("senha2")

        if s1 and s2 and s1 != s2:
            raise forms.ValidationError("As senhas não coincidem.")

        return cleaned_data

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

