from django.db import models


class Anexo(models.Model):
    arquivo = models.FileField(upload_to="anexos/")  # Upload do arquivo
    descricao = models.CharField(max_length=255, blank=True)  # Descrição opcional
    criado_em = models.DateTimeField(auto_now_add=True)  # Data em que o anexo foi enviado

    def __str__(self):
        return f"Anexo: {self.descricao or self.arquivo.name}"
