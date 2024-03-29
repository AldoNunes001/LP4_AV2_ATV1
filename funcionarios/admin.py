from django.contrib import admin
from .models import Departamento, Dependente, Funcionario

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Dependente)
admin.site.register(Departamento)
