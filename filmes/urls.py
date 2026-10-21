
from django.urls import path
from . import views

app_name = 'filmes'

urlpatterns = [
    path('', views.listar_projetos, name='listar_projetos'),
    path('<int:pk>/editar/', views.editar_projeto, name='editar_projeto'),
    path('<int:pk>/excluir/', views.excluir_projeto, name='excluir_projeto'),
    path("tarefas/", views.listar_tarefas, name="listar_tarefas"),
    path("tarefas/nova/", views.criar_tarefa, name="criar_tarefa"),
    path("tarefas/<int:pk>/editar/", views.editar_tarefa, name="editar_tarefa"),
    path("tarefas/<int:pk>/excluir/", views.excluir_tarefa, name="excluir_tarefa"),
]
