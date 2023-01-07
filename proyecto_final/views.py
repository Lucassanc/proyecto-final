from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from proyecto_final.models import Post, Avatar
from django.urls import reverse_lazy
from proyecto_final.forms import UsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, "proyecto_final/index.html", {})

def Nosotros(request):
    return render(request, "proyecto_final/sobrenosotros.html", {})

class PostrDetalle(DetailView):
    model = Post

class PostList(ListView):
    model = Post

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("pag_listar")
    fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("pag_listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("pag_listar")
    fields = '__all__'

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("pag_listar")

class UserLogin(LoginView):
    next_page = reverse_lazy("pag_listar")

class UserLogout(LogoutView):
    next_page = reverse_lazy("pag_index")

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy("pag_listar")

