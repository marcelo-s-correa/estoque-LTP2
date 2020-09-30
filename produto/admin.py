from django.contrib import admin
from .models import Produtos, Cores

class ProdutosAdmin(admin.ModelAdmin):
    list_display = [
        'produto',
        'cor',
        'preco',
        'quantidade',
        ]
    


admin.site.register(Produtos, ProdutosAdmin)
admin.site.register(Cores)