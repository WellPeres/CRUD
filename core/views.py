from django.shortcuts import render, redirect
from .models import Pessoa

def index(request):
    pessoas = Pessoa.objects.all()
    dados = {
        'nomes' : pessoas
    }
    print(dados)
    return render(request, 'index.html', dados)

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'estudos/home.html', {'pessoas': pessoas})

def salvar(request):
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    dados = Pessoa(nome = nome, ultimo_nome = sobrenome)
    dados.save()
    pessoas = Pessoa.objects.all()
    return render(request, 'estudos/home.html', {'pessoas': pessoas})

def editar(request, id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request, 'estudos/edit.html', {'pessoa': pessoa})

def update(request, id):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = nome
    pessoa.ultimo_nome = sobrenome
    pessoa.save()
    return redirect(home)

def delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)
