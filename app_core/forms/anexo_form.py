from django import forms
from ..models.anexo import Anexo


class AnexoForm(forms.ModelForm):
    class Meta:
        model = Anexo
        fields = ['arquivo', 'descricao']  # Campos para upload e descrição
