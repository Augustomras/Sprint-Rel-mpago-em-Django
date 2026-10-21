
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Projeto
from .forms import ProjetoForm


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
