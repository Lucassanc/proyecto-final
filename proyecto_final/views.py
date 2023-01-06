from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from proyecto_final.models import Post
from django.urls import reverse_lazy
from proyecto_final.forms import UsuarioForm

def index(request):
    return render(request, "proyecto_final/index.html", {})

class PostrDetalle(DetailView):
    model = Post

class PostList(ListView):
    model = Post

class PostCrear(CreateView):
    model = Post
    success_url = reverse_lazy("pag_listar")
    fields = '__all__'

class PostBorrar(DeleteView):
    model = Post
    success_url = reverse_lazy("pag_detalle")

class PostActualizar(UpdateView):
    model = Post
    success_url = reverse_lazy("pag_listar")
    fields = '__all__'

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("pag_listar")