from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    context = {}
    usuario = request.user
    publicacoes_list = Publicacao.objects.all().order_by('-data_publicacao')
    paginator = Paginator(publicacoes_list, 6)
    page = request.GET.get('page')
    publicacoes = paginator.get_page(page)
    context['publicacoes'] = publicacoes
    context['usuario'] = usuario
    return render(request, 'index.html', context)


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
    return redirect('/')


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


@login_required(login_url='/')
def editar_perfil(request):
    usuario = request.user
    return render(request, 'editar-perfil.html', {'usuario': usuario})


@login_required(login_url='/')
def submit_editar_perfil(request):
    if request.POST:
        usuario = request.user
        nome = request.POST.get('first_name')
        sobrenome = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        User.objects.filter(id=usuario.id).update(first_name=nome,
                                                  last_name=sobrenome,
                                                  username=username,
                                                  email=email)
        return redirect('/minha_pagina/')


@login_required(login_url='/')
def minha_pagina(request):
    context = {}
    usuario = request.user
    publicacoes = Publicacao.objects.filter(autor=usuario)
    context['publicacoes'] = publicacoes
    context['usuario'] = usuario
    return render(request, 'minha-pagina.html', context)


@login_required(login_url='/')
def escrever_publicacao(request):
    context = {}
    usuario = request.user
    form = editorForm(request.POST or None, request.FILES or None)
    context['usuario'] = usuario
    context['form'] = form
    if request.POST:
        if form.is_valid():
            objeto = form.save(commit=False)
            objeto.autor = usuario
            objeto.save()
            return redirect('/minha_pagina/')
    return render(request, 'escrever-publicacao.html', context)


def publicacao(request, titulo_publicacao):
    context = {}
    usuario = request.user
    publicacao = Publicacao.objects.get(titulo=titulo_publicacao)
    if publicacao:
        context['publicacao'] = publicacao
        if usuario:
            context['usuario'] = usuario
    return render(request, 'publicacao.html', context)


def comentar_publicacao(request, titulo_publicacao):
    if request.POST:
        nome = request.POST.get('nome')
        id_publicacao = request.POST.get('id_publicacao')
        comentario = request.POST.get('comentario')
        if comentario is not None:
            Comentarios.objects.create(nome=nome,
                                       comentario=comentario,
                                       publicacao= get_object_or_404(Publicacao, id=id_publicacao))
    return redirect(f'/publicacao/{titulo_publicacao}/#comentarios')