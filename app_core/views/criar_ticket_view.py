from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Ticket
from ..forms import TicketForm
from django.http import HttpResponseForbidden


@login_required
def criar_ticket(request):
    # Garante que só vem do painel (ou você pode validar outras condições aqui)
    if request.META.get('HTTP_REFERER') is None or 'painel/' not in request.META.get('HTTP_REFERER'):
        msg = "Acesso não permitido digitando o path da URL.<br>Precisa seguir o fluxo do seu atendimento: clicando nos botões correspondentes."
        return HttpResponseForbidden(msg)  # Retorna erro 403 se o acesso for direto

    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.criado_por = request.user
            ticket.save()
            return redirect("lista_tickets")
    else:
        form = TicketForm()
    return render(request, "app_core/criar_ticket.html", {"form": form})
