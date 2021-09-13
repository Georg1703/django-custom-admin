from django import forms
from django.forms import ModelForm
from .models import OrderTicket


class OrderTicketForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    order = forms.CharField(widget=forms.HiddenInput(), required=False)
