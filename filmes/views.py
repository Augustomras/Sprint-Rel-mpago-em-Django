
from django.shortcuts import render, redirect
from .models import Projeto
from .forms import ProjetoForm


def listar_projetos(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('filmes:listar_projetos')
    else:
        form = ProjetoForm()

    projetos = Projeto.objects.all()

    return render(request, 'filmes/listar_projetos.html', {
        'form': form,
        'projetos': projetos
    })
