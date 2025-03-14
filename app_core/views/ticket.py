from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Ticket
from ..forms import TicketForm


@login_required  # Garante que apenas usuários logados acessem
def criar_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)  # Não salva ainda, para adicionar o "criado_por"
            ticket.criado_por = request.user  # Adiciona o usuário logado
            ticket.save()
            return redirect("lista_tickets")  # Redireciona para a página de lista (crie uma URL para isso)
    else:
        form = TicketForm()
    return render(request, "criar_ticket.html", {"form": form})
