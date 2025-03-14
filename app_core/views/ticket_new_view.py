# views/ticket.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_core.models import Ticket  # Importe o modelo (iremos criar ele em breve)


def ticket_new_view(request):
    if request.method == "POST":
        # Processa os dados do formulário aqui
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")

        # Salva o ticket no banco
        Ticket.objects.create(titulo=titulo, descricao=descricao)

        # Redireciona para a lista de tickets após criar
        return redirect("tickets_list")

    # Se a requisição for GET, exibe o formulário
    return render(request, "app_core/ticket_new.html")
