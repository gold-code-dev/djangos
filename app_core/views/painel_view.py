from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def painel_view(request):
    usuario = request.user
    nome_completo = usuario.get_full_name() or usuario.username  # Nome completo ou username
    first_name = usuario.first_name or usuario.username  # Primeiro nome ou username

    # Obter todos os usuários do escritório (exemplo, ajuste para seu modelo)
    usuarios = User.objects.all()

    context = {
        'nome_completo': nome_completo,
        'first_name': first_name,
        'escritorio': "Escritório Modelo",  # Substitua por uma variável ou busca no banco de dados
        'usuarios': usuarios,  # Incluímos a lista de usuários
    }
    return render(request, 'app_core/painel.html', context)
