from django import forms
from .models import Funcionario

class ProfileForm(forms.ModelForm):
    sobrenome = forms.CharField(max_length=30, required=False, help_text="Opcional")
    telefone = forms.CharField(max_length=30, required=False, help_text="Opcional")
    email = forms.EmailField(max_length=120, help_text="Digite seu endereço de email")
    class Meta:
        model = Funcionario
        fields = ['nome', 
                'sobrenome', 
                'telefone', 
                'email', 
                'departamentos', 
                'foto_funcionatio'
                ]
