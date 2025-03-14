from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    TIPO_CHOICES = [
        ('abertura', 'Abertura'),
        ('alteracao', 'Alteração'),
        ('transformacao', 'Transformação'),
        ('baixa', 'Baixa'),
    ]

    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    nome_empresa = models.CharField(max_length=255)
    prazo = models.DateTimeField()
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona ao usuário logado
    criado_em = models.DateTimeField(auto_now_add=True)  # Preenchido automaticamente com a data/hora da criação

    def __str__(self):
        return f"Ticket {self.id} - {self.nome_empresa}"
