from django.shortcuts import render

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