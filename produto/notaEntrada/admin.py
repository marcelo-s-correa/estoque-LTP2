from django.contrib import admin
from .models import NotasEntradas

class notaEntradaAdmin(admin.ModelAdmin):
    list_display = [
        'quantidade',
        'preco',
        'criado',
        ]

admin.site.register(NotasEntradas,notaEntradaAdmin)
