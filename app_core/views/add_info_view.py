from django.shortcuts import render, get_object_or_404
from ..models import Ticket, InformacaoAdicional


def add_info(request, numero_escritorio):
    # Busca o ticket correspondente ou retorna 404
    ticket = get_object_or_404(Ticket, numero_escritorio=numero_escritorio)

    if request.method == "POST":
        # Supondo que a nova informação vem do formulário
        nova_informacao = request.POST.get("nova_informacao")
        # Cria e salva o registro vinculado
        InformacaoAdicional.objects.create(ticket=ticket, informacao=nova_informacao)
        # Redireciona, por exemplo, para a página do ticket
        return redirect("detalhes_ticket", numero_escritorio=numero_escritorio)

    return render(request, "add_info.html", {"ticket": ticket})
