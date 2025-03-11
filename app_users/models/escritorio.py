from django.db import models
from django.contrib.auth.models import User


class Escritorio(models.Model):
    contador = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='escritorio',
        limit_choices_to={'is_staff': False},  # O contador é um usuário regular, não staff
    )

    def __str__(self):
        return f"Escritório de {self.contador.first_name}"
