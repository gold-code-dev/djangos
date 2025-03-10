from django.db import models
from django.contrib.auth.models import User


class Escritorio(models.Model):
    nome = models.CharField(max_length=255)
    logomarca = models.ImageField(upload_to='escritorios/logomarcas/', blank=True, null=True)
    usuarios = models.ManyToManyField(User, related_name='escritorios', blank=True)

    def __str__(self):
        return self.nome