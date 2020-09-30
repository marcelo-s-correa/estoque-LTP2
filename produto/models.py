from django.db import models

class Cores(models.Model):
    cor = models.CharField('Cor', max_length = 200)

    def __str__(self):
        return self.cor

class Produtos(models.Model):
    produto = models.CharField('Produto', max_length = 200)
    slug = models.SlugField('Identificador', max_length=100)
    cor = models.ForeignKey(Cores, on_delete=models.PROTECT, verbose_name='Cor')
    descricao = models.TextField('Descrição', blank=True)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    quantidade = models.IntegerField('Quantidade', default=0)

    criado = models.DateTimeField('Criado em', auto_now_add=True)
    modificado = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-produto']

    def __str__(self):
        return self.produto

    def valorEstoque(self):
        return self.preco * self.quantidade

        