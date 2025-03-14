from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.exceptions import ValidationError


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
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona ao usuário logado # TODO deletar nunca
    criado_em = models.DateTimeField(auto_now_add=True)  # Preenchido automaticamente com a data/hora da criação

    def clean(self):
        """Validação personalizada para o prazo."""
        if self.prazo < now():
            raise ValidationError("O prazo deve ser no futuro ou no presente.")  # Bloqueia data no passado

    def save(self, *args, **kwargs):
        """Executa a validação no momento de salvar o objeto."""
        self.full_clean()  # Verifica todas as validações antes de salvar
        super().save(*args, **kwargs)  # Salva o ticket no banco de dados

    def __str__(self):
        return f"Ticket {self.id} - {self.nome_empresa}"
