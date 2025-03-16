from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseNotAllowed


def login_view(request):
    if request.user.is_authenticated:
        # Redireciona para 'painel' se o usuário já estiver logado
        return redirect('painel')

    if request.method == 'POST':
        # Limpa e normaliza a entrada
        username = request.POST.get('username', '').strip().lower()  # Remove espaços e transforma em minúsculas
        password = request.POST.get('password', '').strip()  # Remove espaços

        if not username or not password:
            # Verificação de campos ausentes
            return render(
                request,
                'login.html',
                {'error': 'Os campos de usuário e senha são obrigatórios!'}
            )

        # Autentica o usuário com as credenciais fornecidas
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Após login, redirecionar para a rota 'painel'
            return redirect('painel')
        else:
            return render(
                request,
                'login.html',
                {'error': 'Senha ou email incorretos!'}
            )

    elif request.method == 'GET':
        return render(request, 'login.html')

    # Resposta para métodos não permitidos
    return HttpResponseNotAllowed(['GET', 'POST'])
