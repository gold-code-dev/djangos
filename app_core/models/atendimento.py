from django.db import models
from django.contrib.auth.models import User
from .escritorio import Escritorio  # Importação do modelo Escritório (relacionamento)


class Atendimento(models.Model):
    id = models.AutoField(primary_key=True)
    nome_empresa = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona ao usuário logado
    criado_em = models.DateTimeField(auto_now_add=True)  # Preenchido automaticamente com a data/hora da criação
    escritorio = models.ForeignKey(Escritorio, on_delete=models.CASCADE,
                                   related_name='atendimentos')  # Relaciona ao Escritório
    numero_escritorio = models.PositiveIntegerField()  # Numeração do atendimento dentro do escritório

    def save(self, *args, **kwargs):
        """Adiciona a lógica para o número único por escritório."""
        if not self.pk:  # Apenas para novos objetos
            ultimo_atendimento = Atendimento.objects.filter(escritorio=self.escritorio).order_by(
                'numero_escritorio').last()
            if ultimo_atendimento:
                self.numero_escritorio = ultimo_atendimento.numero_escritorio + 1
            else:
                self.numero_escritorio = 1  # Primeiro atendimento do escritório

        super().save(*args, **kwargs)  # Salva o atendimento no banco de dados

    def __str__(self):
        return f"Atendimento {self.numero_escritorio} - {self.nome_empresa}"
