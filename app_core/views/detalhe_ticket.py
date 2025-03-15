from django.shortcuts import render, get_object_or_404
from ..models import Ticket


def detalhe_ticket(request, ticket_id):
    # Buscando o ticket específico pelo ID ou exibindo erro 404, caso não exista
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Renderizando o template com o ticket selecionado
    return render(request, 'app_core/detalhe_ticket.html', {'ticket': ticket})

