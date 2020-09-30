from django.contrib import admin
from django.urls import path, include
from produto.views import index, deletar, novo, alterar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entrada/', include('notaEntrada.urls', namespace = 'notaEntrada')),
    path('produto/', include('produto.urls', namespace = 'produto')),
    path('', index, name = 'index'),




]
