from django import forms
from .models import Writer


class WriterForm(forms.ModelForm):

    class Meta:
        model = Writer
        fields = ['name', 'avatar']
        labels = {
            'name': 'Имя',
            'avatar': "Аватар",
        }

