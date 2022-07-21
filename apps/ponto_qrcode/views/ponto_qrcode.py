from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json

from models.ponto_model import PontosQrCodeModel
from funcionarios.models import Funcionario
from funcionarios.forms import ProfileForm


def bate_ponto(request):
    pontos = PontosQrCodeModel.objects.all()
    nome = request.get.POST()
    if request.method == "POST":
        nome = pontos.create(nome=nome)
        messages.success(request, "Ponto batido com sucesso")