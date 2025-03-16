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
    id_atendimento_escritorio = models.PositiveIntegerField()  # ID sequencial do atendimento dentro do escritório

    def save(self, *args, **kwargs):
        """Adiciona a lógica para o ID único por escritório."""
        if not self.pk:  # Apenas para novos objetos
            ultimo_atendimento = Atendimento.objects.filter(
                escritorio=self.escritorio
            ).order_by('id_atendimento_escritorio').last()

            if ultimo_atendimento:
                self.id_atendimento_escritorio = ultimo_atendimento.id_atendimento_escritorio + 1
            else:
                self.id_atendimento_escritorio = 1  # Primeiro atendimento do escritório

        super().save(*args, **kwargs)  # Salva o atendimento no banco de dados

    def __str__(self):
        return f"Atendimento {self.id_atendimento_escritorio} - {self.nome_empresa}"
