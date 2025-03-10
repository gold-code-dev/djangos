from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


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
                {'error': 'Credenciais inválidas'}
            )

    return render(request, 'app_users/login.html')


# View para o painel (login obrigatório)
@login_required  # Certifica que somente usuários autenticados podem acessar
def painel_view(request):
    return render(
        request,
        'app_users/painel.html',
        {
            'username': request.user.username,  # Nome do usuário
            'email': request.user.email,  # Email do usuário
        }
    )
