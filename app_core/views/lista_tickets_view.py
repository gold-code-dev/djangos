from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Ticket


@login_required
def lista_tickets(request):
    tickets = Ticket.objects.filter(criado_por=request.user)  # Apenas os tickets do usuário autenticado
    return render(request, "app_core/lista_tickets.html", {"tickets": tickets})
