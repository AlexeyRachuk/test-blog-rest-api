from django import forms
from django.forms import TextInput, EmailInput, Textarea

from .models import ContactForm


class FormOnContacts(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['form_name', 'form_email', 'form_text']
        widgets = {
            "form_name": TextInput(attrs={
                'class': 'form-control mr-0 ml-auto',
                'placeholder': 'Ваше имя',
            }),
            "form_email": EmailInput(attrs={
                'class': 'form-control mr-0 ml-auto',
                'placeholder': 'Email',
            }),
            "form_text": Textarea(attrs={
                'class': 'form-control mr-0 ml-auto',
                'placeholder': 'Сообщение',
                'rows': 8,
            })
        }
