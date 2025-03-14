from django.db import models
from .tarefa import Tarefa  # Importa o modelo Tarefa
from .anexo import Anexo  # Importa o modelo Anexo


class TarefaAnexo(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE, related_name="anexos")
    anexo = models.ForeignKey(Anexo, on_delete=models.CASCADE, related_name="tarefas")
    criado_em = models.DateTimeField(auto_now_add=True)  # Data automática de criação da relação

    class Meta:
        unique_together = ("tarefa", "anexo")  # Garante que a mesma tarefa e anexo só possam ser vinculados uma vez

    def __str__(self):
        return f"Tarefa ID {self.tarefa.id} - Anexo ID {self.anexo.id}"
