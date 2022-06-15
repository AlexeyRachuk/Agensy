from django import forms
from django.forms import TextInput, Textarea

from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = FormContactPage
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control form-control-lg form-control-a',
                'placeholder': 'Ваше имя',
            }),
            "email": TextInput(attrs={
                'class': 'form-control form-control-lg form-control-a',
                'placeholder': 'Ваш email',
            }),
            "subject": TextInput(attrs={
                'class': 'form-control form-control-lg form-control-a',
                'placeholder': 'Тема обращения',
            }),
            "message": Textarea(attrs={
                'class': 'form-control form-control-lg form-control-a',
                'rows': '5',
                'placeholder': 'Тема обращения',
            })

        }
