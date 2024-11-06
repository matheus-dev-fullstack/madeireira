from django.shortcuts import render, get_object_or_404
# from .forms import TermoForm
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponse
import tempfile
from xhtml2pdf import pisa
from django.urls import reverse_lazy
import os
from django.template.loader import render_to_string
from termo.models import Equipamento, Termo, Usuario
from django.views.generic.edit import UpdateView
from rolepermissions.decorators import has_permission_decorator



@has_permission_decorator('cadastrar_produtos')

def list_terms(request):
    terms = Termo.objects.all()
    return render(request, 'index.html', {'terms': terms})
@has_permission_decorator('cadastrar_produtos')

def list_users(request):
    users = Usuario.objects.all()
    return render(request, 'list_users.html', {'users': users})
@has_permission_decorator('cadastrar_produtos')

def get_term(request, id):
    get_term_data = get_object_or_404(Termo, id=id)
    
    diff_days = None
    if get_term_data.dt_fim and get_term_data.dt_inicio:
            diff_days = (get_term_data.dt_fim - get_term_data.dt_inicio).days
            
    context = {
        'term': get_term_data,
        'diff_days': diff_days
    }
    
    if get_term_data.tipo == 'Permanente':
        return render(request, 'term_permanent.html', context)
    elif get_term_data.tipo == 'Emprestimo':
        return render(request, 'term_emprestimo.html', context)
    else:
        return render(request, '404.html', context)
    
class TermoUpdateView(UpdateView):
    model = Termo
    fields = ['usuario', 'equipamento', 'tipo', 'dt_inicio', 'dt_fim', 'descricao']
    template_name = 'termo_edit.html'
    success_url = reverse_lazy('list-terms') 
@has_permission_decorator('cadastrar_produtos')

def editar_termo(request, id=None):
    if id:
        termo = get_object_or_404(Termo, id=id)
    else:
        termo = None

    if request.method == 'POST':
        form = TermoForm(request.POST, instance=termo)
        if form.is_valid():
            form.save()  # Salva o termo no banco de dados
            return redirect('list-terms')  # Redireciona após o sucesso (defina essa view ou template)
    else:
        form = TermoForm(instance=termo)
    
    return render(request, 'editar_termo.html', {'form': form})

@has_permission_decorator('cadastrar_produtos')
def search_term(request):

    query = request.GET.get('query', '')
    
    if not query:
        return JsonResponse({'results': []})
    
    results = Termo.objects.filter(
        Q(equipamento__icontains=query) |
        Q(usuario__icontains=query) |
        Q(tipo__icontains=query)
    )
    
    results_data = list(results.values('id', 'equipamento', 'usuario', 'tipo'))
    
    return JsonResponse({'results': results_data})
# def print_pdf(request, id):

@has_permission_decorator('cadastrar_produtos')

def render_pdf_view(request, id):
    termo = Termo.objects.get(id=id)
    
    template_path = 'term_permanent.html' 
    context = {'term': termo}
    html = render_to_string(template_path, context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="documento_{id}.pdf"'
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Erro ao gerar PDF', status=400)
    return response
