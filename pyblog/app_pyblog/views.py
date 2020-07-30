from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/minha_pagina/')
        else:
            messages.error(request, 'Usuário e/ou senha inválida')
    return redirect('/login/')

def cadastrar_user(request):
    return render(request, 'cadastrar-usuario.html')

def submit_cadastro_user(request):
    if request.POST:
        nome = request.POST.get('first_name')
        sobrenome = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if nome is not None and sobrenome is not None and username is not None and email is not None and password is not None:
            User.objects.create_user(first_name=nome,
                                     last_name=sobrenome,
                                     username=username,
                                     email=email,
                                     password=password)
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('/minha_pagina/')
        else:
            messages.error(request, 'Preencha todos os campos')

@login_required(login_url='/login/')
def minha_pagina(request):
    usuario = request.user
    return render(request, 'minha-pagina.html', {'usuario': usuario})