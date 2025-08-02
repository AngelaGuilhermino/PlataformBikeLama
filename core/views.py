def login_email(request):
    return render(request, 'login_email.html')

def login_senha(request):
    return render(request, 'login_senha.html')
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def perfil(request):
    return render(request, 'perfil.html')

def cadastro(request):
    return render(request, 'cadastro.html')
