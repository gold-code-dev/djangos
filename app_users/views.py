from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseNotAllowed


# View para exibir e processar login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('painel')  # Após login, redireciona para o painel
        else:
            return render(
                request,
                'app_users/login.html',
                {'error': 'Senha ou email incorretos!'}
            )

    return render(request, 'app_users/login.html')


# View para o painel (login obrigatório)
# @login_required  # Certifica que somente usuários autenticados podem acessar
# def painel_view(request):
#     return render(
#         request,
#         'app_users/painel.html',
#         {
#             'full_name': request.user.get_full_name,  # Nome do completo usuário
#             'email': request.user.email,  # Email do usuário
#         }
#     )


def logout_view(request):
    if request.method == 'POST':
        logout(request)  # Faz o logout
        return redirect('login')  # Redireciona para a tela de login
    return HttpResponseNotAllowed(['POST'])  # Bloqueia métodos como GET


# novo aqui

# views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Escritorio, RelacaoColaborador


# @login_required
# def painel_view(request):
#     context = {}
#
#     Verifica se é contador ou colaborador
    # if hasattr(request.user, 'escritorio'):  # O usuário é contador
    #     escritorio = request.user.escritorio
    #     colaboradores = RelacaoColaborador.objects.filter(escritorio=escritorio)
    #     context['escritorio'] = escritorio
    #     context['usuarios'] = [escritorio.contador] + [colaborador.colaborador for colaborador in colaboradores]
    #
    # elif hasattr(request.user, 'colaboracao'):  # O usuário é colaborador
    #     colaboracao = request.user.colaboracao
    #     escritorio = colaboracao.escritorio
    #     colaboradores = RelacaoColaborador.objects.filter(escritorio=escritorio)
    #     context['escritorio'] = escritorio
    #     context['usuarios'] = [escritorio.contador] + [colaborador.colaborador for colaborador in colaboradores]
    #
    # return render(request, "painel.html", context)
#

"""
@login_required
def painel_view(request):
    context = {}

    # Verifique se é contador
    if hasattr(request.user, 'escritorio'):  # Usuário é contador
        escritorio = request.user.escritorio
        context['tipo_usuario'] = 'contador'
        context['usuarios'] = [escritorio.contador]

    # Verifique se é colaborador
    elif hasattr(request.user, 'colaboracao'):  # Usuário é colaborador
        colaboracao = request.user.colaboracao
        escritorio = colaboracao.escritorio
        context['tipo_usuario'] = 'colaborador'
        context['usuarios'] = [colaboracao.colaborador]

    # Renderiza o painel com o contexto preenchido
    return render(request, "app_users/painel.html", context)
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Escritorio, RelacaoColaborador

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

    return render(request, "app_users/painel.html", context)
