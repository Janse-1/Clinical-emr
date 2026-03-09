from django.contrib import admin
from .models import Doctor, Paciente, Expediente

admin.site.register(Doctor)
admin.site.register(Paciente)
admin.site.register(Expediente)