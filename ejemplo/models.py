from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

class Pacientes(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=200)
    edad = models.IntegerField()
    observaciones = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.nombre}, {self.tipo}, {self.edad}, {self.observaciones}"

class Operarios(models.Model):
    nombre = models.CharField(max_length=100)
    legajo = models.IntegerField()
    categoria = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.nombre}, {self.legajo}, {self.categoria}, {self.observaciones}"