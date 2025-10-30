from django.urls import path
from .views import (
    EventoListView,
    EventoDetailView,
    EventoCreateView,
    EventoUpdateView,
    EventoDeleteView,
    CiclistaDeleteView,
    InscricaoDeleteView,
    UserDeleteView,
)

urlpatterns = [
    path('', EventoListView.as_view(), name='evento_list'),
    path('create/', EventoCreateView.as_view(), name='evento_create'),
    path('<int:pk>/', EventoDetailView.as_view(), name='evento_detail'),
    path('<int:pk>/edit/', EventoUpdateView.as_view(), name='evento_update'),
    path('<int:pk>/delete/', EventoDeleteView.as_view(), name='evento_delete'),

    # Admin-only deletes
    path('ciclista/<str:pk>/delete/', CiclistaDeleteView.as_view(), name='ciclista_delete'),
    path('inscricao/<int:pk>/delete/', InscricaoDeleteView.as_view(), name='inscricao_delete'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]