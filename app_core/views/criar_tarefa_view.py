from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Tarefa, Ticket, Anexo
from ..forms.tarefa_form import TarefaForm


@login_required
def criar_tarefa(request, numero_ticket):  # O parâmetro numero_ticket é obrigatório
    # Tenta buscar o Ticket pelo número. Gera erro 404 se não encontrar.
    ticket = get_object_or_404(Ticket, numero_escritorio=numero_ticket)

    # Recupera os anexos associados ao Ticket
    anexos = Anexo.objects.filter(ticket=ticket)

    if request.method == 'POST':
        # Processa o formulário enviado, incluindo o ticket_id para filtrar anexos no formulário
        form = TarefaForm(request.POST, ticket_id=ticket.id)
        if form.is_valid():
            tarefa = form.save(commit=False)  # Cria o objeto tarefa sem salvar ainda no banco
            tarefa.criado_por = request.user  # Define o criador da tarefa como o usuário logado
            tarefa.ticket = ticket  # Associa a tarefa ao ticket
            tarefa.save()  # Salva a tarefa no banco de dados

            # Recupera os anexos selecionados no formulário e cria as relações
            anexos_selecionados = form.cleaned_data['anexos']
            for anexo in anexos_selecionados:
                tarefa.anexos.add(anexo)  # Vincula o anexo à tarefa (de acordo com o modelo)

            return redirect('/tarefas/')  # Redireciona para a lista de tarefas ou outra URL desejada
    else:
        # Inicializa o formulário vazio com os anexos do ticket
        form = TarefaForm(ticket_id=ticket.id)

    # Renderiza o formulário, passando informações do ticket e anexos
    return render(
        request,
        'criar_tarefa.html',
        {'form': form, 'ticket': ticket, 'anexos': anexos}
    )