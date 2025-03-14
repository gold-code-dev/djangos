from django.db import models
from .ticket import Ticket  # Importa o modelo Ticket
from .tarefa_anexo import TarefaAnexo  # Importa o modelo TarefaAnexo


class TicketTarefaAnexo(models.Model):
    numero_escritorio = models.IntegerField()  # Campo vindo do Ticket
    tarefa_anexo = models.ForeignKey(TarefaAnexo, on_delete=models.CASCADE, related_name="tickets")
    criado_em = models.DateTimeField(auto_now_add=True)  # Data automática de criação

    class Meta:
        unique_together = ("numero_escritorio", "tarefa_anexo")  # Garante que essa combinação seja única

    def __str__(self):
        return f"Ticket {self.numero_escritorio} - Tarefa/Anexo ID {self.tarefa_anexo.id}"
