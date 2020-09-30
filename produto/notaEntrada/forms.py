from django import forms
from .models import NotasEntradas
from django.forms import Textarea, TextInput, NumberInput,Select

class FormNotasEntradas(forms.ModelForm):
    preco = forms.DecimalField(widget = NumberInput(attrs={'class':'valores'}),
localize=True)

    class Meta:
        model = NotasEntradas
        fields = [
            'produto',
            'quantidade',
            'preco',
        ]
        widgets = {
            'preco':NumberInput(attrs={'step': 0.5, 'style':'font: 1rem Fira Sans, sans-serif; color:green; width: 16.5%','placeholder':'100,00'}),
            'produto':Select(attrs={'style':'width: 16.5%'}),
            'quantidade':NumberInput(attrs={'style':'width: 16.5%'})
            }
