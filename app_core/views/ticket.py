from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms import TicketForm  # Importamos o formulário da nova pasta
from ..models.ticket import Ticket


def criar_ticket_view(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            novo_ticket = form.save(commit=False)
            novo_ticket.usuario = request.user  # Relacionamos o ticket ao usuário logado
            novo_ticket.save()
            messages.success(request, "Ticket criado com sucesso!")
            return redirect('/')  # Ajuste o redirecionamento conforme sua necessidade
    else:
        form = TicketForm()

    return render(request, 'ticket.html', {'form': form})
