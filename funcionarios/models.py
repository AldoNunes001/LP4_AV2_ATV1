from django.db import models


# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=15)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    cargo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_contratacao = models.DateField()

    def __str__(self):
        return self.nome


class Dependente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=15)
    funcionario = models.ForeignKey(
        Funcionario, on_delete=models.CASCADE, related_name="dependentes"
    )

    def __str__(self):
        return self.nome


class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    funcionarios = models.ManyToManyField(Funcionario, related_name="departamentos")

    def __str__(self):
        return self.nome
