from django.urls import path
from .views import EventoListView, EventoDetailView, EventoCreateView, EventoUpdateView, EventoDeleteView, CiclistaDeleteView, InscricaoDeleteView, UserDeleteView
from core.views import calendario, eventos, passeios, cadastro, formInscricoes, autenticacao, desconectar, perfil, index


urlpatterns = [
    path('', index, name='index'),
    path('calendario/', calendario, name='calendario'),
    path('eventos/', eventos, name='eventos'),
    path('passeios/', passeios, name='passeios'),
    path('formCadastro/', cadastro, name='formCadastro'),
    path('perfil/', perfil, name='perfil'),
    path('formInscricoes/', formInscricoes, name='formInscricoes'),
    path('formLogin/', autenticacao, name='formLogin'),
    path('desconectar/', desconectar, name='desconectar'),


    path('', EventoListView.as_view(), name='evento_list'),
    path('create/', EventoCreateView.as_view(), name='evento_create'),
    path('<int:pk>/', EventoDetailView.as_view(), name='evento_detail'),
    path('<int:pk>/edit/', EventoUpdateView.as_view(), name='evento_update'),
    path('<int:pk>/delete/', EventoDeleteView.as_view(), name='evento_delete'),

    # Admin deletes
    path('ciclista/<str:pk>/delete/', CiclistaDeleteView.as_view(), name='ciclista_delete'),
    path('inscricao/<int:pk>/delete/', InscricaoDeleteView.as_view(), name='inscricao_delete'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]