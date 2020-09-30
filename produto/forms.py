from django.forms import ModelForm
from .models import Produtos
from django.forms import Textarea, TextInput, NumberInput,Select

class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields = [
        'produto',
        'preco',
        'quantidade',
        'cor']
        widgets = {
            'preco':NumberInput(attrs={'step': 0.5, 'style':'font: 1rem Fira Sans, sans-serif; color:green; width: 16.5%','placeholder':'100,00'}),
            'produto':TextInput(attrs={'style':'width: 16.5%'}),
            'quantidade':NumberInput(attrs={'style':'width: 16.5%'}),
            'cor': Select(attrs={'style':'width: 16.5%'})
            }
