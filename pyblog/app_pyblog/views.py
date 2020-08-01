from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *

# Create your views here.

def index(request):
    context = {}
    publicacoes = Publicacao.objects.all().order_by('-data_publicacao')[:6]
    context['publicacoes'] = publicacoes
    return render(request, 'index.html', context)

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
    context = {}
    usuario = request.user
    publicacoes = Publicacao.objects.filter(autor=usuario)
    context['publicacoes'] = publicacoes
    context['usuario'] = usuario
    return render(request, 'minha-pagina.html', context)

@login_required(login_url='/login/')
def escrever_publicacao(request):
    context = {}
    usuario = request.user
    form = editorForm(request.POST or None)
    context['usuario'] = usuario
    context['form'] = form
    if request.POST:
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.autor = usuario
            objeto.save()
            return redirect('/minha_pagina/')
    return render(request, 'escrever-publicacao.html', context)

@login_required(login_url='/login/')
def publicacao(request, id_publicacao):
    context = {}
    publicacao = Publicacao.objects.get(id=id_publicacao)
    if publicacao:
        context['publicacao'] = publicacao
    return render(request, 'publicacao.html', context)