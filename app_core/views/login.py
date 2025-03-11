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
            return redirect('base')  # Após login, redireciona para o painel
        else:
            return render(
                request,
                'app_core/login.html',
                {'error': 'Senha ou email incorretos!'}
            )

    return render(request, 'app_core/login.html')