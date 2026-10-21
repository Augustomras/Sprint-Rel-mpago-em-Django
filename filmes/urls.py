
from django.urls import path
from . import views

app_name = 'filmes'

urlpatterns = [
    path('', views.listar_projetos, name='listar_projetos'),
    path('<int:pk>/editar/', views.editar_projeto, name='editar_projeto'),
    path('<int:pk>/excluir/', views.excluir_projeto, name='excluir_projeto'),
]
