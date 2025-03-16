from django.shortcuts import render, redirect
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

    # Verifica se o número do ticket foi passado via GET, para redirecionar
    numero_ticket = request.GET.get("numero_ticket")  # Captura o número do ticket
    if numero_ticket:
        # Aqui aplicamos a regra de negócio: redirecionamento para criar tarefa
        return redirect("criar_tarefa", numero_ticket=numero_ticket)

    # Caso não haja número do ticket nos parâmetros, renderizamos a página normalmente
    return render(request, "app_core/lista_tickets.html", {"tickets": tickets})
