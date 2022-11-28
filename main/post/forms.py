from django import forms
from django.forms import TextInput, Textarea

from .models import Comments


class FormComments(forms.ModelForm):
    """Форма для комметариев"""

    class Meta:
        model = Comments
        fields = ['comment_name', 'comment_text']
        widgets = {
            "comment_name": TextInput(attrs={
                'class': 'form-control mr-0 ml-auto',
                'placeholder': 'Ваше имя',
            }),
            "comment_text": Textarea(attrs={
                'class': 'form-control mr-0 ml-auto',
                'placeholder': 'Ваше комментарий',
                'rows': 5,
            })
        }
