from django.shortcuts import render, get_object_or_404, redirect
from ..models import Ticket, Anexo  # Importar os modelos envolvidos
from ..forms.anexo_form import AnexoForm  # Importar o formulário de anexos


def detalhe_ticket(request, ticket_id):
    # Buscar o ticket específico pelo ID ou exibir erro 404 se não encontrar
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Buscar todos os anexos relacionados ao ticket
    anexos = ticket.anexos.all()

    # Verificar se está enviando um anexo via POST
    if request.method == 'POST':
        form = AnexoForm(request.POST, request.FILES)
        if form.is_valid():
            anexo = form.save(commit=False)
            anexo.ticket = ticket  # Associar o anexo ao ticket atual
            anexo.save()
            return redirect('detalhe_ticket', ticket_id=ticket_id)  # Recarregar a página após o upload
    else:
        # Criar o formulário vazio para o upload de novos anexos
        form = AnexoForm()

    # Renderizar o template e passar os dados do ticket, anexos e formulário
    return render(request, 'ticket_detalhe.html', {
        'ticket': ticket,
        'anexos': anexos,
        'form': form,
    })
