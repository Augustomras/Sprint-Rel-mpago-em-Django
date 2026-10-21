
from django import forms
from .models import Projeto
from .models import Tarefa


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao']

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ["titulo", "descricao", "concluida", "projeto"]
        widgets = {
            "projeto": forms.Select(),
        }