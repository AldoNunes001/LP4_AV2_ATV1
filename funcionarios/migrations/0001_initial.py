# Generated by Django 5.0.3 on 2024-03-29 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Funcionario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("idade", models.IntegerField()),
                ("telefone", models.CharField(max_length=15)),
                ("salario", models.DecimalField(decimal_places=2, max_digits=8)),
                ("cargo", models.CharField(max_length=100)),
                ("descricao", models.TextField()),
                ("data_contratacao", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Dependente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("idade", models.IntegerField()),
                ("telefone", models.CharField(max_length=15)),
                (
                    "funcionario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dependentes",
                        to="funcionarios.funcionario",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Departamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                (
                    "funcionarios",
                    models.ManyToManyField(
                        related_name="departamentos", to="funcionarios.funcionario"
                    ),
                ),
            ],
        ),
    ]
