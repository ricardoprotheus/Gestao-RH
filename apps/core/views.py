from multiprocessing import context
from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants

from funcionarios.models import Funcionario

#@login_required
def home(request):
    data = {}
    data['usuario'] =  request.user
    context = {
        'data': data,
    }
    return render(request, "core/index.html", context)

def logar(request):
    if request.method == 'GET':
        # Se o ususario já estiver logado, será direcionado para pagina principal
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'core/index.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')

        # existe um usuario e senha igual o que foi digitado?
        usuario = auth.authenticate(username=username, password=senha)
        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha incorreto!')
            return redirect('/accounts/login/')
        else:
            auth.login(request, usuario) #logar e ser redirecionado para a raiz do sistema
            return redirect('/')
            
def logout_request(request):
    logout(request)
    return redirect("home")
