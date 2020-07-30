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

@login_required(login_url='/login/')
def minha_pagina(request):
    usuario = request.user
    return render(request, 'minha-pagina.html', {'usuario': usuario})