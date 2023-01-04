from django.shortcuts import render
from django.views.generic import ListView, CreateView
from proyecto_final.models import Post
from django.urls import reverse_lazy

def index(request):
    return render(request, "proyecto_final/index.html", {})

class PostList(ListView):
    model = Post

class PostCrear(CreateView):
    model = Post
    success_url = "pag_listar"
    fields = '__all__'