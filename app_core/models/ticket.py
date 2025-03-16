from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from .escritorio import Escritorio  # Importação do modelo Escritório (relacionamento)


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
    escritorio = models.ForeignKey(Escritorio, on_delete=models.CASCADE,
                                   related_name='tickets')  # Relaciona ao Escritório
    numero_escritorio = models.PositiveIntegerField()  # Numeração do ticket dentro do escritório

    def clean(self):
        """Validação personalizada para o prazo."""
        if self.prazo < now():
            raise ValidationError("O prazo deve ser no futuro ou no presente.")  # Bloqueia data no passado

    def save(self, *args, **kwargs):
        """Adiciona a lógica para o número único por escritório."""
        if not self.pk:  # Apenas para novos objetos
            ticket_ultimo = Ticket.objects.filter(escritorio=self.escritorio).order_by('numero_escritorio').last()
            if ticket_ultimo:
                self.numero_escritorio = ticket_ultimo.numero_escritorio + 1
            else:
                self.numero_escritorio = 1  # Primeiro ticket do escritório

        self.full_clean()  # Executa validação
        super().save(*args, **kwargs)  # Salva o ticket no banco de dados

    def __str__(self):
        return f"Ticket {self.numero_escritorio} - {self.nome_empresa}"
