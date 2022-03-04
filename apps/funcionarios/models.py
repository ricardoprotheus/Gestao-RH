from django.db import models
from django.contrib.auth.models import User
from departamentos.models import Departamento
from empresas.models import Empresa

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do funcionário")
    sobrenome = models.CharField(max_length=100, null=False, blank=False,help_text="Sobre nome do funcionario")
    telefone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=80, null=False, blank=False, help_text="E-mail")
    #Criar user junto ao cadastro(protegido) USUARIO UNICO PARA UM FUNCIONARIO
    user = models.OneToOneField(User, on_delete=models.PROTECT) 
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    foto_funcionatio = models.ImageField(upload_to=nome)

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(Self):
        return Self.nome