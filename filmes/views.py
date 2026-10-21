
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Projeto
from .forms import ProjetoForm
from .models import Tarefa
from .forms import TarefaForm


def listar_projetos(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto cadastrado com sucesso!')
            return redirect('filmes:listar_projetos')
    else:
        form = ProjetoForm()

    projetos = Projeto.objects.all()

    return render(request, 'filmes/listar_projetos.html', {
        'form': form,
        'projetos': projetos
    })


def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('filmes:listar_projetos')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'filmes/editar_projeto.html', {
        'form': form,
        'projeto': projeto
    })


def excluir_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)

    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto excluído com sucesso!')
        return redirect('filmes:listar_projetos')

    return render(request, 'filmes/excluir_projeto.html', {
        'projeto': projeto
    })

def listar_tarefas(request):
    tarefas = Tarefa.objects.select_related("projeto").all()
    return render(request, "filmes/tarefa_list.html", {
        "tarefas": tarefas
    })


def criar_tarefa(request):
    form = TarefaForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("listar_tarefas")

    return render(request, "filmes/tarefa_form.html", {
        "form": form,
        "titulo": "Criar tarefa"
    })


def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    form = TarefaForm(request.POST or None, instance=tarefa)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("listar_tarefas")

    return render(request, "filmes/tarefa_form.html", {
        "form": form,
        "titulo": "Editar tarefa"
    })


def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == "POST":
        tarefa.delete()
        return redirect("listar_tarefas")

    return render(request, "filmes/tarefa_confirm_delete.html", {
        "tarefa": tarefa
    })