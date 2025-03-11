from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseNotAllowed


def logout_view(request): # colocar que somente usuario logado pode deslogar? 
    if request.method == 'POST':
        logout(request)  # Faz o logout
        return redirect('login')  # Redireciona para a tela de login
    return HttpResponseNotAllowed(['POST'])  # Bloqueia métodos como GET

