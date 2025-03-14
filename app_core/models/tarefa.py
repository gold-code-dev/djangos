from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Tarefa(models.Model):
    nome = models.CharField(max_length=255)  # Nome descritivo da tarefa
    descricao = models.TextField(blank=True)  # Descrição detalhada da tarefa
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tarefas_criadas")  # Criador da tarefa
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name="tarefas_responsaveis")  # Responsável pela execução
    concluido = models.BooleanField(default=False)  # Flag para saber se foi concluída
    criado_em = models.DateTimeField(auto_now_add=True)  # Data de criação automática
    prazo = models.DateTimeField(blank=True, null=True)  # Prazo final para concluir a tarefa

    class Meta:
        ordering = ["-criado_em"]  # Ordenação das tarefas pela data de criação (mais recente primeiro)
        verbose_name_plural = "Tarefas"

    def is_atrasada(self):
        """Verifica se a tarefa está atrasada."""
        if self.prazo and not self.concluido and now() > self.prazo:
            return True
        return False

    def __str__(self):
        return f"Tarefa: {self.nome} (Concluída: {'Sim' if self.concluido else 'Não'})"
