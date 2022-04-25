from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Empresa

class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome', ]
