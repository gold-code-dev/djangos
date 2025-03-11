from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def base_view(request):
    usuario = request.user
    nome_completo = usuario.get_full_name()

    # Se o nome completo estiver em branco (o que costuma ser o padrão), use o username.
    if not nome_completo:
        nome_completo = usuario.username

    context = {'nome_completo': nome_completo}
    return render(request, 'app_users/base.html', context)
