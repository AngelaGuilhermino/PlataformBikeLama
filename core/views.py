from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def calendario(request):
    return render(request, 'calendario.html')

def inscricoes(request):
    return render(request, 'inscricoes.html')

def telainicial(request):
    return render(request, 'telainicial.html')

def eventos(request):
    return render(request, 'eventos.html')