from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Usuário deve estar logado para criar uma tarefa
from ..models import Tarefa
from ..forms.tarefa_form import TarefaForm


@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        # Instancia o formulário com os dados submetidos via POST
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)  # Cria o objeto tarefa sem salvar ainda
            tarefa.criado_por = request.user  # Define o usuário atual como criador
            tarefa.save()  # Salva a tarefa no banco de dados
            return redirect('/tarefas/')  # Redireciona para a listagem ou outra página
    else:
        # Exibe o formulário vazio para criação
        form = TarefaForm()

    # Renderiza o template com o formulário
    return render(request, 'app_core/criar_tarefa.html', {'form': form})
