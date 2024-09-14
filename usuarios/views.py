from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator
from .models import Users

@has_permission_decorator('cadastrar_vendedor')
def cadastrar_vendedor(request):
    if request.method == 'GET':
        return render(request, 'cadastrar_vendedor.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = Users.objects.filter(email=email)
        
        if user.exists():
            # TODO: utilizar messages do django
            return HttpResponse('Já existe um vendedor com este email')
        
        user = Users.objects.create_user(username=email, email=email, password=senha)
        
        # TODO: Redirecionar com uma mensagem
        return HttpResponse('Vendedor criado com sucesso')