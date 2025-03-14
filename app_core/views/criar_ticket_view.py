from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Ticket
from ..forms import TicketForm
from django.http import HttpResponseForbidden


@login_required
def criar_ticket(request):
    # Garante que só vem do painel (se necessário)
    if request.META.get('HTTP_REFERER') is None or 'painel/' not in request.META.get('HTTP_REFERER'):
        return HttpResponseForbidden(
            "Acesso não permitido: entre pelo seu painel para criar tickets."
        )  # Retorna 403 se acesso for direto

    # Lógica para salvar o ticket
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)  # Não salva imediatamente
            ticket.criado_por = request.user  # Associa o ticket ao usuário logado

            # Verifica se o usuário é contador ou colaborador para associar ao escritório
            if hasattr(request.user, 'escritorio'):
                ticket.escritorio = request.user.escritorio  # Contador
            elif hasattr(request.user, 'colaboracao'):
                ticket.escritorio = request.user.colaboracao.escritorio  # Colaborador

            ticket.save()  # Salva o ticket no banco
            return redirect("lista_tickets")  # Redireciona para a lista de tickets

    else:
        form = TicketForm()  # Formulário vazio para GET (primeiro carregamento)

    # Renderiza o formulário
    return render(
        request,
        "app_core/criar_ticket.html",
        {"form": form}  # Apenas o formulário é enviado ao template
    )
