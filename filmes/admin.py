
from django.contrib import admin
from .models import Projeto
from .models import Tarefa

admin.site.register(Tarefa)

admin.site.register(Projeto)
