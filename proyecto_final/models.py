from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    publicado_el = models.DateField()
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=3000)

class Avatar(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="avatar")
    imagen = models.ImageField(upload_to="avatares", null="True", blank=True)