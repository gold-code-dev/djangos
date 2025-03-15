from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from ..models import Anx
from ..models import Ticket  # Certifique-se de ajustar o caminho de importação do modelo Ticket


class AnxCreateView(View):
    """
    View para criar um novo Anexo sem usar Form
    """

    def post(self, request, *args, **kwargs):
        try:
            # Busca o ticket com base no ID enviado na requisição
            ticket_id = request.POST.get('ticket_id')
            ticket = get_object_or_404(Ticket, id=ticket_id)

            # Obtém os dados do arquivo enviado e o nome do anexo
            arquivo = request.FILES.get('arquivo')  # Arquivo enviado
            nome = request.POST.get('nome')  # Nome/descrição enviada para o anexo

            if not arquivo or not nome:
                return JsonResponse({'erro': 'Nome do anexo e arquivo são obrigatórios.'}, status=400)

            # Cria o anexo no banco de dados
            anexo = Anx.objects.create(
                nome=nome,
                arquivo=arquivo,
                ticket=ticket  # Relaciona o Ticket ao anexo (supondo que há essa FK no modelo)
            )

            # Retorna o ID/criação do item com sucesso
            return JsonResponse({
                'mensagem': 'Anexo criado com sucesso!',
                'id': anexo.id,
                'nome': anexo.nome,
                'url_arquivo': anexo.arquivo.url,
                'ticket': anexo.ticket.id,
            }, status=201)

        except Exception as e:
            return JsonResponse({'erro': str(e)}, status=500)
