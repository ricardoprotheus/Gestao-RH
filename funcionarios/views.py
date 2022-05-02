from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario
