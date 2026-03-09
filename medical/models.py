from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    especialidad = models.CharField(max_length=150)
    numero_colegiado = models.CharField(max_length=50)
    firma = models.ImageField(upload_to='firmas/', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    identificacion = models.CharField(max_length=50)

    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    sexo = models.CharField(max_length=10)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Expediente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    fecha_consulta = models.DateField()

    motivo_consulta = models.TextField()
    antecedentes = models.TextField()

    diagnostico = models.TextField()
    procedimiento = models.TextField()

    medicacion = models.TextField()
    observaciones = models.TextField()

    resumen = models.TextField()

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Expediente {self.paciente.nombre} - {self.fecha_consulta}"