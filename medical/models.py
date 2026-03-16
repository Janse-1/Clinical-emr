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

    paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Expediente {self.id} - {self.paciente.nombre}"
    
    
class FichaIdentificacion(models.Model):

    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE)

    ocupacion = models.CharField(max_length=150)
    residencia = models.CharField(max_length=200)

    estado_civil = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=100)

    religion = models.CharField(max_length=100)

    cama = models.CharField(max_length=20)
    servicio = models.CharField(max_length=100)

    escolaridad = models.CharField(max_length=100)

    telefono_contacto = models.CharField(max_length=20)
    
    
class AntecedentesHeredofamiliares(models.Model):

    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE)

    padre_vivo = models.BooleanField()
    causa_muerte_padre = models.TextField(blank=True)

    madre_viva = models.BooleanField()
    causa_muerte_madre = models.TextField(blank=True)

    hermanos_vivos = models.IntegerField(default=0)
    hermanos_fallecidos = models.IntegerField(default=0)
    causa_muerte_hermanos = models.TextField(blank=True)

    hijos_vivos = models.IntegerField(default=0)
    hijos_fallecidos = models.IntegerField(default=0)

    diabetes = models.BooleanField(default=False)
    hipertension = models.BooleanField(default=False)
    tuberculosis = models.BooleanField(default=False)
    cancer = models.BooleanField(default=False)

    otras_enfermedades = models.TextField(blank=True)
    
class AntecedentesNoPatologicos(models.Model):

    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE)

    alcohol = models.BooleanField(default=False)
    tabaco = models.BooleanField(default=False)
    drogas = models.BooleanField(default=False)

    alimentacion = models.TextField(blank=True)
    dipsia = models.TextField(blank=True)
    diuresis = models.TextField(blank=True)
    catarsis = models.TextField(blank=True)
    somnia = models.TextField(blank=True)

    otros = models.TextField(blank=True)
    
class AntecedentesPatologicos(models.Model):

    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE)

    diabetes = models.BooleanField(default=False)
    hipertension = models.BooleanField(default=False)
    tuberculosis = models.BooleanField(default=False)
    cancer = models.BooleanField(default=False)

    otras = models.TextField(blank=True)

    quirurgicos = models.TextField(blank=True)
    traumatologicos = models.TextField(blank=True)
    alergicos = models.TextField(blank=True)

    otros = models.TextField(blank=True)
    

class GinecoObstetricos(models.Model):

    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE)

    fum = models.DateField(null=True, blank=True)

    fpp = models.DateField(null=True, blank=True)

    edad_gestacional = models.IntegerField(null=True, blank=True)

    menarca = models.IntegerField(null=True, blank=True)

    ritmo_menstrual = models.CharField(max_length=100, blank=True)

    numero_parejas = models.IntegerField(null=True, blank=True)

    flujo_genital = models.TextField(blank=True)

    gestas = models.IntegerField(default=0)
    partos = models.IntegerField(default=0)
    cesareas = models.IntegerField(default=0)
    abortos = models.IntegerField(default=0)

    anticonceptivos = models.BooleanField(default=False)

    tipo_anticonceptivo = models.CharField(max_length=100, blank=True)

    tiempo_anticonceptivo = models.CharField(max_length=100, blank=True)

    ultima_toma = models.DateField(null=True, blank=True)

    cirugias_ginecologicas = models.TextField(blank=True)

    otros = models.TextField(blank=True)
    

class PadecimientoActual(models.Model):

    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE)

    descripcion = models.TextField()
    
    
class InterrogatorioSistemas(models.Model):

    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE)

    respiratorio = models.TextField(blank=True)
    digestivo = models.TextField(blank=True)
    cardiovascular = models.TextField(blank=True)
    renal_urinario = models.TextField(blank=True)
    genital = models.TextField(blank=True)
    endocrino = models.TextField(blank=True)
    hematopoyetico = models.TextField(blank=True)
    piel = models.TextField(blank=True)
    musculo_esqueletico = models.TextField(blank=True)
    sistema_nervioso = models.TextField(blank=True)
    organos_sentidos = models.TextField(blank=True)
    sintomas_generales = models.TextField(blank=True)
    

class ExploracionFisica(models.Model):

    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE)

    impresion_general = models.TextField()

    fc = models.IntegerField(null=True, blank=True)
    ta = models.CharField(max_length=20)
    fr = models.IntegerField(null=True, blank=True)

    pulso = models.IntegerField(null=True, blank=True)

    peso = models.FloatField(null=True, blank=True)
    talla = models.FloatField(null=True, blank=True)

    bmi = models.FloatField(null=True, blank=True)

    temperatura = models.FloatField(null=True, blank=True)

    inspeccion_general = models.TextField(blank=True)

    cabeza = models.TextField(blank=True)
    cuello = models.TextField(blank=True)
    torax = models.TextField(blank=True)
    abdomen = models.TextField(blank=True)

    tacto_vaginal_rectal = models.TextField(blank=True)

    extremidades = models.TextField(blank=True)

    exploracion_neurologica = models.TextField(blank=True)
    

class Diagnostico(models.Model):

    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE)

    diagnostico_presuntivo = models.TextField()
    
    
class PlanTerapeutico(models.Model):

    expediente = models.OneToOneField(Expediente, on_delete=models.CASCADE)

    plan = models.TextField()