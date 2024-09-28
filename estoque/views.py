from django.shortcuts import render
from .models import Categoria,Produto,Imagem
from django.http import HttpResponse

# Create your views here.
def add_produto(request):

    if request.method == "GET":
        categoria = Categoria.objects.all()
        return render(request, 'add_produto.html', {'categorias': categoria})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        categoria= request.POST.get('categoria')
        quantidade = request.POST.get('quantidade')
        preco_compra = request.POST.get('preco_compra')
        preco_venda = request.POST.get('preco_venda')
        
        produto = Produto(nome=nome, 
                        categoria_id=categoria,
                        quantidade=quantidade,
                        preco_compra=preco_compra,
                        preco_venda=preco_venda)
        
        produto.save()
        
        for f in request.FILES.getlist('imagens'):
            img = Imagem(imagem = f, produto = produto)
            img.save()
        
        return HttpResponse('Foi')
        