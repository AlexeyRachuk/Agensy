from django import forms
from django.forms import TextInput, Textarea

from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = FormContactPage
        fields = ['name', 'subject', 'message']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control form-control-lg form-control-a',
                'placeholder': 'Ваше имя',
            }),
            "subject": TextInput(attrs={
                'class': 'form-control form-control-lg form-control-a',
                'placeholder': 'Способ связи',
            }),
            "message": Textarea(attrs={
                'class': 'form-control form-control-lg form-control-a',
                'rows': '5',
                'placeholder': 'Сообщение',
            })

        }
