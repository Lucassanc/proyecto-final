from django.shortcuts import render, get_object_or_404
from ejemplo.models import Familiar
from ejemplo.forms import Buscar, FamiliarForm
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView


class FamiliarDetalle(DetailView):
    model = Familiar

class FamiliarList(ListView):
  model = Familiar

class FamiliarCrear(CreateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte"]

class FamiliarBorrar(DeleteView):
  model = Familiar
  success_url = "/panel-familia"

class FamiliarActualizar(UpdateView):
  model = Familiar
  success_url = "/panel-familia"
  fields = ["nombre", "direccion", "numero_pasaporte"]

