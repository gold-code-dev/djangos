from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('recebido', 'Recebido'),
        ('enviado', 'Enviado'),
        ('elaboracao', 'Em Elaboração'),
    ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='elaboracao')
    criado_em = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
