from django.db import models
from produto.models import Produtos

class NotasEntradas(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.PROTECT)
    quantidade = models.IntegerField('Quantidade', default=0)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    criado = models.DateTimeField('Criado em', auto_now_add=True)
    modificado = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-produto']

    def __str__(self):
        return self.produto.produto


