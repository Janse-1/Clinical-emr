from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm

def dashboard(request):
    return render(request, 'dashboard.html')

def lista_pacientes(request):
    pacientes = Paciente.objects.all().order_by('-fecha_creacion')
    return render(request, 'pacientes/lista_pacientes.html', {'pacientes': pacientes})


def crear_paciente(request):

    if request.method == 'POST':
        form = PacienteForm(request.POST)

        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.save()
            return redirect('lista_pacientes')

    else:
        form = PacienteForm()

    return render(request, 'pacientes/crear_paciente.html', {'form': form})


def editar_paciente(request, id):

    paciente = get_object_or_404(Paciente, id=id)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)

        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')

    else:
        form = PacienteForm(instance=paciente)

    return render(request, 'pacientes/editar_paciente.html', {'form': form})


def eliminar_paciente(request, id):

    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()

    return redirect('lista_pacientes')