from django import forms
from ..models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['tipo', 'nome_empresa', 'prazo']  # Campos que o usuário pode preencher
        widgets = {
            'prazo': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
