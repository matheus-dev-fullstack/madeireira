from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages

@has_permission_decorator('cadastrar_vendedor')
def cadastrar_vendedor(request):
    if request.method == 'GET':
        vendedores = Users.objects.filter(cargo='V')
        return render(request, 'cadastrar_vendedor.html', {'vendedores': vendedores} )
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = Users.objects.filter(email=email)
        
        if user.exists():
            messages.add_message(request, messages.ERROR, 'Já existe um vendedor com este email.')
            return redirect(reverse('cadastrar_vendedor'))
        
        user = Users.objects.create_user(username=email, email=email, password=senha, cargo='V')
        
        messages.add_message(request, messages.SUCCESS, 'Vendedor criado com sucesso.')
        return redirect(reverse('cadastrar_vendedor'))
    
def login(request):
    if request.method == "GET":
        if request.user.is_authenticated: 
            return redirect(reverse('plataforma'))
        return render(request, 'login.html')
    
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(username=login, password=senha)
        
        if not user:
            messages.add_message(request, messages.ERROR, 'Usuário ou senha inválidos')
            return redirect(reverse('login'))
        
        auth.login(request, user)
        return HttpResponse('Usuário logado com sucesso')
    
def logout(request):
    request.session.flush()
    return redirect(reverse('login'))

@has_permission_decorator('cadastrar_vendedor')
def excluir_usuario(request, id):
    vendedor = get_object_or_404(Users, id=id)
    vendedor.delete()
    messages.add_message(request, messages.SUCCESS, 'Vendedor excluído com sucesso')
    return redirect(reverse('cadastrar_vendedor'))