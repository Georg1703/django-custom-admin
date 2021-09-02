from django.forms import ModelForm
from .models import OrderTicket


class OrderTicketForm(ModelForm):

    class Meta:
        model = OrderTicket
        fields = ('value',)