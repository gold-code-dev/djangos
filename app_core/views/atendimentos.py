# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import AtendimentoForm
from ..models import Atendimento


@login_required
def criar_atendimento(request):
    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            atendimento = form.save(commit=False)
            atendimento.criado_por = request.user
            atendimento.save()
            return redirect('listar_atendimentos')
    else:
        form = AtendimentoForm()

    return render(request, 'criar_atendimento.html', {'form': form})


@login_required
def lista_atendimentos(request):
    atendimentos = Atendimento.objects.all().order_by('-criado_em')
    return render(request, 'lista_atendimentos.html', {'atendimentos': atendimentos})


@login_required
def detalhe_atendimento(request, atendimento_id):
    atendimento = get_object_or_404(Atendimento, id=atendimento_id)
    return render(request, 'detalhe_atendimento.html', {'atendimento': atendimento})
