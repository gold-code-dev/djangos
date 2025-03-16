# forms.py
from django import forms
from ..models import Atendimento


class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['nome_empresa', 'escritorio']
        # Note que 'id', 'criado_por', 'criado_em' e 'id_atendimento_escritorio' são preenchidos automaticamente

    def __init__(self, *args, **kwargs):
        super(AtendimentoForm, self).__init__(*args, **kwargs)
        self.fields['nome_empresa'].widget.attrs.update({'class': 'form-control'})
        self.fields['escritorio'].widget.attrs.update({'class': 'form-control'})
