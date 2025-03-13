from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponseNotAllowed


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)  # Faz o logout
        return redirect('login')  # Redireciona para a tela de login
    return HttpResponseNotAllowed(['POST'])  # Permite apenas método POST
