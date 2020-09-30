from django.urls import path
from .views import notaEntradaList, notaEntradaNew

app_name = 'notaEntrada'
urlpatterns = [
    path('notaEntradaList/', notaEntradaList, name='notaEntradaList'),
    path('notaEntradaNew/', notaEntradaNew, name='notaEntradaNew'),
]
