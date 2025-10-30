from django.contrib import admin
from .models import Ciclista, TipoEvento, Evento, Inscricao

@admin.register(Ciclista)
class CiclistaAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'email', 'cidade', 'estado')
    search_fields = ('cpf', 'nome', 'email')

@admin.register(TipoEvento)
class TipoEventoAdmin(admin.ModelAdmin):
    list_display = ('descricao',)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome_evento', 'data_evento', 'valor_inscricao', 'tipoEvento')
    list_filter = ('data_evento', 'tipoEvento')
    search_fields = ('nome_evento',)

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('ciclista', 'evento', 'data_inscricao', 'status')
    list_filter = ('status',)
    search_fields = ('ciclista__nome', 'evento__nome_evento')
