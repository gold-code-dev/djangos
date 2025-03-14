from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Ticket


@login_required
def lista_tickets(request):
    # Verifica o tipo de usuário logado e consulta os tickets associados ao escritório
    if hasattr(request.user, 'escritorio'):  # Usuário é contador
        tickets = Ticket.objects.filter(escritorio=request.user.escritorio).order_by('-criado_em')

    elif hasattr(request.user, 'colaboracao'):  # Usuário é colaborador
        tickets = Ticket.objects.filter(escritorio=request.user.colaboracao.escritorio).order_by('-criado_em')

    else:
        # Usuário não associado a nenhum escritório
        tickets = Ticket.objects.none()  # Nenhum ticket será listado

    return render(request, "app_core/lista_tickets.html", {"tickets": tickets})
