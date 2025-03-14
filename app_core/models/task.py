from django.db import models


class Task(models.Model):
    titulo = models.CharField(max_length=200)  # Título da tarefa
    descricao = models.TextField(blank=True)  # Descrição opcional
    prazo = models.DateTimeField(null=True, blank=True)  # Prazo opcional
    concluida = models.BooleanField(default=False)  # Status da tarefa
    criado_em = models.DateTimeField(auto_now_add=True)  # Data de criação

    def __str__(self):
        return f"Tarefa: {self.titulo}"
