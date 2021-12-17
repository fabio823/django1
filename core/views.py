from django.shortcuts import render, get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader

def index(request):
    #print(dir(request))
    #print(f'User: {dir(request.user)}')
    #print(f'User: {request.user.last_login}')

    '''
    if str(request.user) == "AnonymousUser":
        resposta = "Usuário não logado"
    else:
        resposta = "Usuário logado!!!"
    '''

    produtos = Produto.objects.all()
    context = {
        "curso": "Programação web com Django Framework",
        "outro": "Django é massa!!!!",
        "produtos": produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    #print(f'ID: {id}')
    #prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id)
    context = {
        "contemProduto": prod,
    }
    return render(request, 'produto.html', context)

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return  HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
