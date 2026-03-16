from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Paciente, Expediente
from .forms import ( PacienteForm, FichaIdentificacionForm,
    AntecedentesHeredofamiliaresForm,
    AntecedentesNoPatologicosForm,
    AntecedentesPatologicosForm,
    GinecoObstetricosForm,
    PadecimientoActualForm,
    InterrogatorioSistemasForm,
    ExploracionFisicaForm,
    DiagnosticoForm,
    PlanTerapeuticoForm
    ) 
from datetime import date

def dashboard(request):

    query = request.GET.get('q')

    pacientes = Paciente.objects.all()
    expedientes = Expediente.objects.select_related('paciente')
    
    if query:
        pacientes = pacientes.filter(
            Q(nombre__icontains=query) |
            Q(identificacion__icontains=query)
        )

    pacientes = pacientes.order_by('-fecha_creacion')[:10]

    total_pacientes = Paciente.objects.count()

    context = {
        'pacientes': pacientes,
        'expedientes': expedientes,
        'total_pacientes': total_pacientes,
        'consultas_hoy': 0,
        'total_expedientes': total_pacientes
    }

    return render(request,'dashboard.html',context)

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


#Expediente Views
def expediente_paciente(request, paciente_id):

    paciente = get_object_or_404(Paciente, id=paciente_id)

    expediente, created = Expediente.objects.get_or_create(
        paciente=paciente
    )

    if request.method == "POST":

        ficha_form = FichaIdentificacionForm(request.POST)
        heredo_form = AntecedentesHeredofamiliaresForm(request.POST)
        nopato_form = AntecedentesNoPatologicosForm(request.POST)
        pato_form = AntecedentesPatologicosForm(request.POST)
        gineco_form = GinecoObstetricosForm(request.POST)
        padecimiento_form = PadecimientoActualForm(request.POST)
        interrogatorio_form = InterrogatorioSistemasForm(request.POST)
        exploracion_form = ExploracionFisicaForm(request.POST)
        diagnostico_form = DiagnosticoForm(request.POST)
        plan_form = PlanTerapeuticoForm(request.POST)

        if (
            ficha_form.is_valid()
            and heredo_form.is_valid()
            and nopato_form.is_valid()
            and pato_form.is_valid()
            and gineco_form.is_valid()
            and padecimiento_form.is_valid()
            and interrogatorio_form.is_valid()
            and exploracion_form.is_valid()
            and diagnostico_form.is_valid()
            and plan_form.is_valid()
        ):

            ficha = ficha_form.save(commit=False)
            ficha.expediente = expediente
            ficha.save()

            heredo = heredo_form.save(commit=False)
            heredo.expediente = expediente
            heredo.save()

            nopato = nopato_form.save(commit=False)
            nopato.expediente = expediente
            nopato.save()

            pato = pato_form.save(commit=False)
            pato.expediente = expediente
            pato.save()

            gineco = gineco_form.save(commit=False)
            gineco.expediente = expediente
            gineco.save()

            padecimiento = padecimiento_form.save(commit=False)
            padecimiento.expediente = expediente
            padecimiento.save()

            interrogatorio = interrogatorio_form.save(commit=False)
            interrogatorio.expediente = expediente
            interrogatorio.save()

            exploracion = exploracion_form.save(commit=False)
            exploracion.expediente = expediente
            exploracion.save()

            diagnostico = diagnostico_form.save(commit=False)
            diagnostico.expediente = expediente
            diagnostico.save()

            plan = plan_form.save(commit=False)
            plan.expediente = expediente
            plan.save()

            return redirect("ver_expediente", expediente.id)

    else:

        ficha_form = FichaIdentificacionForm()
        heredo_form = AntecedentesHeredofamiliaresForm()
        nopato_form = AntecedentesNoPatologicosForm()
        pato_form = AntecedentesPatologicosForm()
        gineco_form = GinecoObstetricosForm()
        padecimiento_form = PadecimientoActualForm()
        interrogatorio_form = InterrogatorioSistemasForm()
        exploracion_form = ExploracionFisicaForm()
        diagnostico_form = DiagnosticoForm()
        plan_form = PlanTerapeuticoForm()

    context = {

        "paciente": paciente,
        "expediente": expediente,

        "ficha_form": ficha_form,
        "heredo_form": heredo_form,
        "nopato_form": nopato_form,
        "pato_form": pato_form,
        "gineco_form": gineco_form,
        "padecimiento_form": padecimiento_form,
        "interrogatorio_form": interrogatorio_form,
        "exploracion_form": exploracion_form,
        "diagnostico_form": diagnostico_form,
        "plan_form": plan_form,

    }

    return render(request, "expedientes/form_expediente.html", context)


def ver_expediente(request, expediente_id):

    expediente = get_object_or_404(Expediente, id=expediente_id)

    return render(
        request,
        "expedientes/ver_expediente.html",
        {"expediente": expediente}
    )
