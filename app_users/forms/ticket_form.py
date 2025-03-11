from django import forms
from ..models.ticket import Ticket  # Importando o modelo Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['titulo', 'descricao', 'status']  # Substitua pelos campos reais do seu modelo
