from django.shortcuts import redirect, render
from .models import veiculos

def index(request):
    veiculo = veiculos.objects.all()
    return render(request,'index.html',{'veiculo':veiculo})

def cadastrar(request):
    return render(request,'cadastrar.html')

def adicionar(request):#addrec
    nom=request.POST['nome']
    color=request.POST['cor']
    monta=request.POST['montadora']
    veiculo=veiculos(nome=nom,cor=color,montadora=monta)
    veiculo.save()
    return redirect("/")

def apagar(request,id):
    veiculo=veiculos.objects.get(id=id)
    veiculo.delete()
    return redirect("/")

def editar(request,id):
    veiculo=veiculos.objects.get(id=id)
    return render(request,'atualizar.html',{'veiculo':veiculo})

def atualizar(request,id):
    nom=request.POST['nome']
    color=request.POST['cor']
    monta=request.POST['montadora']
    veiculo=veiculos.objects.get(id=id)
    veiculo.nome=nom
    veiculo.cor=color
    veiculo.montadora=monta
    veiculo.save()
    return redirect("/")