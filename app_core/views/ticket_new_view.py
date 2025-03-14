from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Para exigir autenticação


@login_required(login_url='/login/')  # Redireciona para '/login/' se não autenticado
def ticket_new_view(request):
    # Apenas renderiza a página HTML (sem passar dados ou tratar POST ainda)
    return render(request, "app_core/ticket_new.html")
