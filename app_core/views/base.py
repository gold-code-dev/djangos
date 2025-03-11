from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def base_view(request):
    usuario = request.user
    nome_completo = usuario.get_full_name()

    # Se o nome completo estiver em branco (o que costuma ser o padrão), use o username
    if not nome_completo:
        nome_completo = usuario.username

    # Obter o primeiro nome do usuário
    first_name = usuario.first_name or usuario.username  # Usa o primeiro nome; caso esteja em branco, usa o username

    context = {
        'nome_completo': nome_completo,
        'first_name': first_name,  # Incluímos o primeiro nome no contexto
    }
    return render(request, 'app_core/base.html', context)
