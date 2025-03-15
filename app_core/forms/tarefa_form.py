from django import forms
from ..models import Tarefa, Anexo


class TarefaForm(forms.ModelForm):
    anexos = forms.ModelMultipleChoiceField(  # Campo para seleção de múltiplos anexos
        queryset=Anexo.objects.none(),  # Inicialmente vazio, será filtrado no __init__
        required=False,
        label="Anexos relacionados",  # Texto do campo
        widget=forms.CheckboxSelectMultiple  # Checkboxes para permitir seleção múltipla
    )

    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao', 'responsavel', 'prazo', 'concluido']

    def __init__(self, *args, **kwargs):
        ticket_id = kwargs.pop('ticket_id', None)  # Recupera o ticket ID da tarefa (passado pela view)
        super().__init__(*args, **kwargs)

        # Filtra os anexos disponíveis com base no ticket atual
        if ticket_id:
            self.fields['anexos'].queryset = Anexo.objects.filter(ticket_id=ticket_id)
        else:
            # Se nenhum ticket for identificado, o campo de anexos é ocultado
            self.fields['anexos'].widget = forms.HiddenInput()
