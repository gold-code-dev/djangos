
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Escritorio, RelacaoColaborador


@login_required
def painel_view(request):
    context = {}

    if hasattr(request.user, 'escritorio'):  # É contador
        escritorio = request.user.escritorio
        colaboradores = RelacaoColaborador.objects.filter(escritorio=escritorio)
        context['tipo_usuario'] = 'contador'
        context['usuarios'] = [escritorio.contador] + [colaborador.colaborador for colaborador in colaboradores]

    elif hasattr(request.user, 'colaboracao'):  # É colaborador
        colaboracao = request.user.colaboracao
        escritorio = colaboracao.escritorio
        colaboradores = RelacaoColaborador.objects.filter(escritorio=escritorio)
        context['tipo_usuario'] = 'colaborador'
        context['usuarios'] = [escritorio.contador] + [colaborador.colaborador for colaborador in colaboradores]

    else:  # Caso o usuário não tenha os atributos necessários
        context['tipo_usuario'] = 'desconhecido'
        context['usuarios'] = []  # Nenhum usuário relacionado

    # return render(request, "app_users/painel.html", context)
    return render(request, "app_users/painel/index.html", context)
