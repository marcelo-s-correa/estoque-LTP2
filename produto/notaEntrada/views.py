from django.shortcuts import render, redirect
from .models import NotasEntradas
from .forms import FormNotasEntradas

def notaEntradaList(request):
    nota_entrada = NotasEntradas.objects.all()
    nota_entrada_ord = NotasEntradas.objects.order_by('criado')
    template_name = 'notaEntradaList.html'
    lst_data = []
    lst_qtd = []
    lst_produtos = []
    for nota in nota_entrada_ord:
        data = nota.criado
        format_data = data.strftime("%d/%m/%Y")
        lst_data.append(format_data)
        lst_produtos.append(str(nota.produto))
        lst_qtd.append(nota.quantidade)

    context = {
        'nota_entrada': nota_entrada,
        'lst_data': lst_data,
        'lst_produtos': lst_produtos,
        'lst_qtd': lst_qtd,
    }
    return render(request, template_name, context)

def notaEntradaNew(request):
    if request.method == "POST":
        form = FormNotasEntradas(request.POST)
        if form.is_valid:
            form.save(commit=False)

            form.cleaned_data['produto'].quantidade = form.cleaned_data['produto'].quantidade + form.cleaned_data['quantidade']

            form.cleaned_data['produto'].preco = form.cleaned_data['preco']
            form.cleaned_data['produto'].save_base()

            form.save()
            return redirect('notaEntrada:notaEntradaList')
    else:
        form = FormNotasEntradas()
        print(form)
        template_name = 'notaEntradaNew.html'
        context = {
            'form': form,
    }
    return render(request, template_name, context)
