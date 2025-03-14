from django.db import models
from .task import Task  # Importando o modelo Task corretamente
from .anexo import Anexo  # Importando o modelo Anexo corretamente


class TarefaAnexo(models.Model):
    tarefa = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,  # Quando a tarefa for deletada, os relacionamentos somem
        related_name="anexos"
    )
    anexo = models.ForeignKey(
        Anexo,
        on_delete=models.CASCADE,  # Quando o anexo for apagado, o vínculo desaparece
        related_name="tarefas"
    )
    criado_em = models.DateTimeField(auto_now_add=True)  # Data de vínculo

    def __str__(self):
        return f"Tarefa: {self.tarefa.titulo} - Anexo: {self.anexo.descricao or self.anexo.arquivo.name}"
