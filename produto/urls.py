from django.urls import path
from .views import index, novo, alterar, deletar

app_name = 'produto'
urlpatterns = [
    path('novo/', novo, name = 'novo'),
    path('deletar/<int:pk>/', deletar, name= 'deletar'),
    path('alterar/<int:pk>/', alterar, name = 'alterar'),
    path('', index, name = 'index'),
]
