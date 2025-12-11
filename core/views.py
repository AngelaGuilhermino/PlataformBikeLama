from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Evento, Ciclista, Inscricao
from .forms import EventoForm, CiclistaForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.POST:
       form = CiclistaForm(request.POST)
       if form.is_valid():
            ciclista = form.save(commit=False)
            ciclista.set_password(form.cleaned_data['senha'])  # cria senha corretamente
            ciclista.save()
            return redirect('formLogin')
    else:
        form = CiclistaForm()

    return render(request, 'formCadastro.html', {'form': form})


@login_required
def perfil(request):
    return render(request, 'perfil.html')

def autenticacao(request):
    if request.POST:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(request, email=email, password=senha)

        if user:
            login(request, user)
            return redirect('perfil')
        else:
            return render(request, 'formLogin.html', {"erro": "Email ou senha incorretos"})

    return render(request, 'formLogin.html')

def desconectar(request):
    logout(request)
    return redirect('index')

def index(request): 
    return render(request, 'index.html')

def calendario(request): 
    return render(request, 'calendario.html')

def eventos(request): 
    return render(request, 'eventos.html')

def passeios(request): 
    return render(request, 'passeios.html')

def formInscricoes(request): 
    return render(request, 'formInscricoes.html')

def formCadastro(request): 
    return render(request, 'formCadastro.html')

def formLogin(request): 
    return render(request, 'formLogin.html')

# CRUD generic views for Evento (now public — no staff/login checks)
class EventoListView(ListView):
    model = Evento
    template_name = 'evento_list.html'
    context_object_name = 'eventos'

class EventoDetailView(DetailView):
    model = Evento
    template_name = 'evento_detail.html'
    context_object_name = 'evento'

class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'evento_form.html'
    success_url = reverse_lazy('evento_list')

class EventoUpdateView(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'evento_form.html'
    success_url = reverse_lazy('evento_list')

class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'evento_confirm_delete.html'
    success_url = reverse_lazy('evento_list')

# Deletion views for Ciclista, Inscricao and User are public now (no staff checks)
class CiclistaDeleteView(DeleteView):
    model = Ciclista
    template_name = 'ciclista_confirm_delete.html'
    success_url = reverse_lazy('evento_list')

class InscricaoDeleteView(DeleteView):
    model = Inscricao
    template_name = 'inscricao_confirm_delete.html'
    success_url = reverse_lazy('evento_list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('evento_list')