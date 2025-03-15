from django import forms
from ..models import Ticket
from django.utils.timezone import now


from ..models import Tarefa, Ticket


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao', 'responsavel', 'prazo', 'concluido', 'ticket']  # Adicione o campo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Tornar o ticket invisível no formulário (caso necessário, por exemplo, se for definido pela view)
        self.fields['ticket'].widget = forms.HiddenInput()
        self.fields['responsavel'].required = True
