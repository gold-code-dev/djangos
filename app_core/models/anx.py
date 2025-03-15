from django.db import models
from datetime import datetime


class Anx(models.Model):
    """
    Modelo para Anexos (Anx)
    """

    # Lógica para gerar o caminho personalizado
    def caminho_arquivo_anexo(instance, filename):
        """
        Gera o caminho para salvar os arquivos enviados usando a data/hora/milissegundos se o ID ainda é inexistente.
        Estrutura do caminho:
        anexos/e_<ID_DO_ESCRITORIO>/t_<ID_DO_TICKET>/a_<DATETIMESTAMP>/<NOME_DO_ARQUIVO>
        """
        id_escritorio = instance.ticket.contador.escritorio.id  # ID do Escritório associado ao Ticket
        id_ticket = instance.ticket.id  # ID do Ticket associado
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')  # Gera o timestamp com data + hora + milissegundos

        return f"anexos/e_{id_escritorio}/t_{id_ticket}/a_{timestamp}/{filename}"

    # Campos do modelo
    nome = models.CharField(max_length=255, verbose_name="Nome do Anexo")  # Nome do arquivo ou descrição do anexo
    arquivo = models.FileField(upload_to=caminho_arquivo_anexo,
                               verbose_name="Arquivo")  # Arquivo com diretório dinâmico
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")  # Data de criação do anexo

    def __str__(self):
        return self.nome
