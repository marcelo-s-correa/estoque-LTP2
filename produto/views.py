from django.shortcuts import render, redirect
from .models import Produtos
from .forms import ProdutoForm

def index(request):
    produtos = Produtos.objects.all()
    template_name = 'index.html'
    lst_produtos = []
    lst_qtd = []
    lst_valorEstoque = [] 
    for produto in produtos :
        lst_produtos.append(produto.produto)
        lst_qtd.append(produto.quantidade)
        lst_valorEstoque.append(float(produto.valorEstoque()))
    print(lst_valorEstoque)
    context = {
        'produtos': produtos,
        'lst_produtos': lst_produtos,
        'lst_qtd':lst_qtd,
        'lst_valorEstoque': lst_valorEstoque,
    }
    return render(request, template_name, context)

def deletar(request,pk):
    produto = Produtos.objects.get(pk=pk)
    produto.delete()
    return redirect('produto:index')

def novo(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto:index')
    else:
        template_name = 'novo.html'
        context = {
            'form': ProdutoForm(),
        }
    return render(request, template_name, context)

def alterar(request,pk):
    produto = Produtos.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto:index')
    else:
        template_name = 'alterar.html'
        context = {
            'form': ProdutoForm(instance=produto),
            'pk': pk,
        }
    return render(request, template_name, context)