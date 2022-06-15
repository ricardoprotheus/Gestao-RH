from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView, UpdateView, 
    DeleteView, CreateView)

from .models import RegistroHoraExtra
from .forms import HoraExtraForm


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = HoraExtraForm
    success_url = reverse_lazy('list_horas_extra')

    # Injetar usuario logado para entro do Form(HoraExtraForm)
    def get_form_kwargs(self):
        Kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        Kwargs.update({'user': self.request.user})
        return Kwargs
    def form_invalid(self, form):
        print("form invalidod")
        print(form.errors)
        messages.add_message(self.request, constants.ERROR, "Hora extra não pode ser criada!")
        return super().form_invalid(form)
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, constants.SUCCESS, "Hora extra cadastrada com sucesso!")
        return super().form_valid(form)


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraUpdate(UpdateView):
    template_name = 'registro_hora_extra/registrohoraextra_form.html'
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']

    def form_invalid(self, form):
        print("form invalidod")
        print(form.errors)
        messages.add_message(self.request, constants.ERROR, "Hora extra não pode ser atualizada!")
        return super().form_invalid(form)

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, constants.SUCCESS, "Hora extra atualizada com sucesso!")
        return super().form_valid(form)


class HoraExtraDelete(SuccessMessageMixin, DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_horas_extra')
    success_message = "Hora extra deletada com sucesso!"

    def delete(self, request, *args, **kwargs):
        if self.get_success_url():
            messages.success(self.request, self.success_message)
            return super(HoraExtraDelete, self).delete(request, *args, **kwargs)

from .models import RegistroHoraExtra
from .forms import HoraExtraForm


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = HoraExtraForm
    success_url = reverse_lazy('list_horas_extra')

    # Injetar usuario logado para entro do Form(HoraExtraForm)
    def get_form_kwargs(self):
        Kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        Kwargs.update({'user': self.request.user})
        return Kwargs
    def form_invalid(self, form):
        print("form invalidod")
        print(form.errors)
        messages.add_message(self.request, constants.ERROR, "Hora extra não pode ser criada!")
        return super().form_invalid(form)
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, constants.SUCCESS, "Hora extra cadastrada com sucesso!")
        return super().form_valid(form)


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraUpdate(UpdateView):
    template_name = 'registro_hora_extra/registrohoraextra_form.html'
    model = RegistroHoraExtra
    form_class = HoraExtraForm
    success_url = reverse_lazy('list_horas_extra')

    # Injetar usuario logado para entro do Form(HoraExtraUpdate)
    # Mostrar apenas usuarios da empresa logada
    def get_form_kwargs(self):
        Kwargs = super(HoraExtraUpdate, self).get_form_kwargs()
        Kwargs.update({'user': self.request.user})
        return Kwargs

    def form_invalid(self, form):
        print("form invalidod")
        print(form.errors)
        messages.add_message(self.request, constants.ERROR, "Hora extra não pode ser atualizada!")
        return super().form_invalid(form)

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, constants.SUCCESS, "Hora extra atualizada com sucesso!")
        return super().form_valid(form)


class HoraExtraDelete(SuccessMessageMixin, DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_horas_extra')
    success_message = "Hora extra deletada com sucesso!"

    def delete(self, request, *args, **kwargs):
        if self.get_success_url():
            messages.success(self.request, self.success_message)
            return super(HoraExtraDelete, self).delete(request, *args, **kwargs)

