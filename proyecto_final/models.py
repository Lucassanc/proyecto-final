from django.db import models

class Post(models.Model):
    publicado_el = models.DateField()
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=3000)