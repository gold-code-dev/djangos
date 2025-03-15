from django.db import models
from .ticket import Ticket  # Relacionar anexo ao ticket


class Anexo(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name="anexos",
        null=True, blank=True  # Caso você permita anexos provisórios (sem ticket)
    )
    arquivo = models.FileField(upload_to="anexos/")  # Upload do arquivo
    descricao = models.CharField(max_length=255, blank=True)  # Descrição opcional
    criado_em = models.DateTimeField(auto_now_add=True)  # Data em que o anexo foi enviado

    def __str__(self):
        return f"Anexo: {self.descricao or self.arquivo.name} do Ticket {self.ticket or 'Sem Ticket'}"
