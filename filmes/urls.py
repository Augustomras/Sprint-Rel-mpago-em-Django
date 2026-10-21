
from django.urls import path
from . import views

app_name = 'filmes'

urlpatterns = [
    path('', views.listar_projetos, name='listar_projetos'),
]
