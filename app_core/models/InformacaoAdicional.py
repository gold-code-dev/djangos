from django.db import models


class Ticket(models.Model):
    numero_escritorio = models.IntegerField(unique=True)
    titulo = models.CharField(max_length=200)


class InformacaoAdicional(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="informacoes_adicionais")
    informacao = models.TextField()
    criada_em = models.DateTimeField(auto_now_add=True)
