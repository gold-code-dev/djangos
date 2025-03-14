from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Tarefa, Ticket
from ..forms.tarefa_form import TarefaForm


@login_required
def criar_tarefa(request, numero_ticket):  # O parâmetro numero_ticket agora é obrigatório
    # Sempre tenta buscar o Ticket pelo número. Gera erro 404 se não encontrar.
    ticket = get_object_or_404(Ticket, numero_escritorio=numero_ticket)

    if request.method == 'POST':
        # Processa o formulário enviado
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)  # Cria o objeto tarefa sem salvar imediatamente
            tarefa.criado_por = request.user  # Define o criador da tarefa como o usuário logado
            tarefa.ticket = ticket  # Associa a tarefa ao ticket obrigatoriamente
            tarefa.save()  # Salva a tarefa no banco de dados
            return redirect('/tarefas/')  # Redireciona para a lista de tarefas (ou outro fluxo desejado)
    else:
        # Exibe o formulário vazio para o usuário preencher
        form = TarefaForm()

    # Renderiza o formulário, passando informações do ticket selecionado
    return render(request, 'app_core/criar_tarefa.html', {'form': form, 'ticket': ticket})
