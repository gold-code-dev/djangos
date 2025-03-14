from django import forms
from ..models import Tarefa


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao', 'responsavel', 'prazo', 'concluido']
        widgets = {
            'prazo': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Estilizar os campos ou alterar as etiquetas, se necessário
        self.fields['responsavel'].required = True  # Torna um campo necessário
