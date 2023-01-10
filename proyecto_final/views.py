from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from proyecto_final.models import Post, Avatar, Mensaje
from django.urls import reverse_lazy
from proyecto_final.forms import UsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


def index(request):
    posts = Post.objects.order_by('-publicado_el')
    return render(request, "proyecto_final/index.html", {"posts": posts})

def Nosotros(request):
    return render(request, "proyecto_final/sobrenosotros.html", {})

def Config(request):
    return render(request, "proyecto_final/config.html", {})

class PostrDetalle(DetailView):
    model = Post

class PostList(LoginRequiredMixin, ListView):
    model = Post

class PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("pag_index")
    fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("pag_index")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("pag_index")
    fields = '__all__'

class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("pag_index")

class UserLogin(LoginView):
    next_page = reverse_lazy("pag_index")

class UserLogout(LogoutView):
    next_page = reverse_lazy("pag_index")

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy("pag_index")

class UserActualizar(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email')
    success_url = reverse_lazy("pag_index")

class MensajeDetalle(LoginRequiredMixin, DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje

class MensajeCrear(LoginRequiredMixin, CreateView):
    model = Mensaje
    success_url = reverse_lazy("pag_index")
    fields = ['nombre', 'email', 'texto']

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("pag_mensaje_listar")