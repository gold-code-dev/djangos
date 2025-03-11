from django.db import models
from django.contrib.auth.models import User
from .escritorio import Escritorio


class RelacaoColaborador(models.Model):
    escritorio = models.ForeignKey(
        Escritorio,
        on_delete=models.CASCADE,
        related_name='colaboradores'
    )
    colaborador = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='colaboracao'
    )

    def __str__(self):
        return f"{self.colaborador.first_name} - Escritório: {self.escritorio}"
