from django.shortcuts import render, redirect
from ..models import Tarefa


def criar_tarefa(request):
    if request.method == 'POST':  # Verifica se os dados estão sendo enviados (via formulário)
        nome = request.POST.get('nome')  # Pega o valor do campo "nome"
        descricao = request.POST.get('descricao')  # Pega o valor do campo "descricao"
        responsavel = request.POST.get('responsavel')  # Pega o valor do campo "responsável"
        prazo = request.POST.get('prazo')  # Pega o prazo (se existir)

        # Criação da nova tarefa no banco de dados
        Tarefa.objects.create(
            nome=nome,
            descricao=descricao,
            responsavel=responsavel,
            prazo=prazo
        )

        # Após criar, redireciona o usuário para a página de listagem (ou outra desejada)
        return redirect('/tarefas/')

    # Caso contrário (GET), exibe o formulário
    return render(request, 'tarefas/criar_tarefa.html')
