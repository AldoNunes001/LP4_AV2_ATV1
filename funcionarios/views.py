# from django.shortcuts import render
from .models import Funcionario
from django.views.generic import ListView, DetailView


# Create your views here.
class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "funcionarios/list.html"
    context_object_name = "funcionarios"

    def get_queryset(self):
        return Funcionario.objects.prefetch_related("dependentes", "departamentos")


class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = "funcionarios/detail.html"
    context_object_name = "funcionario"

    def get_object(self, queryset=None):
        return super().get_object(
            queryset=Funcionario.objects.prefetch_related(
                "dependentes", "departamentos"
            )
        )
