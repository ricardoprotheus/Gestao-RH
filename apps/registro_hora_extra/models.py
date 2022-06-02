from pyexpat import model
from django.db import models
from funcionarios.models import Funcionario

class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=70, help_text="Motivo da Hora Extra")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return self.motivo
