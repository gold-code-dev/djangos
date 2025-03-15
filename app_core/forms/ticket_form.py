from django import forms
from ..models import Ticket
from django.utils.timezone import now


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['tipo', 'nome_empresa', 'prazo']
        widgets = {
            'prazo': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'min': now().strftime('%Y-%m-%dT%H:%M')  # Data e hora mínimas para hoje
            }),
        }