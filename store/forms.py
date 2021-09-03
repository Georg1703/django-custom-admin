from django import forms
from django.forms import ModelForm
from .models import OrderTicket


class OrderTicketForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    order = forms.CharField(widget=forms.HiddenInput(), required=False)
    customer = forms.CharField(widget=forms.HiddenInput(), required=False)
