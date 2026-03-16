from django import forms
from .models import (Paciente, FichaIdentificacion,
        AntecedentesHeredofamiliares,
        AntecedentesNoPatologicos,
        AntecedentesPatologicos,
        GinecoObstetricos,
        PadecimientoActual,
        InterrogatorioSistemas,
        ExploracionFisica,
        Diagnostico,
        PlanTerapeutico
    )

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'fecha_nacimiento',
            'identificacion',
            'telefono',
            'direccion',
            'sexo'
        ]

        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
        
class FichaIdentificacionForm(forms.ModelForm):

    class Meta:
        model = FichaIdentificacion

        fields = "__all__"

        widgets = {

            "ocupacion": forms.TextInput(attrs={"class":"form-control"}),

            "residencia": forms.TextInput(attrs={"class":"form-control"}),

            "estado_civil": forms.Select(attrs={"class":"form-control"}),

            "nacionalidad": forms.TextInput(attrs={"class":"form-control"}),

            "religion": forms.TextInput(attrs={"class":"form-control"}),

            "cama": forms.TextInput(attrs={"class":"form-control"}),

            "servicio": forms.TextInput(attrs={"class":"form-control"}),

            "escolaridad": forms.TextInput(attrs={"class":"form-control"}),

            "telefono_contacto": forms.TextInput(attrs={"class":"form-control"})
        }
        
class AntecedentesHeredofamiliaresForm(forms.ModelForm):

    class Meta:

        model = AntecedentesHeredofamiliares

        fields = "__all__"

        widgets = {

            "padre_vivo": forms.RadioSelect(choices=[(True,"Sí"),(False,"No")]),

            "madre_viva": forms.RadioSelect(choices=[(True,"Sí"),(False,"No")]),

            "causa_muerte_padre": forms.Textarea(attrs={"rows":3}),

            "causa_muerte_madre": forms.Textarea(attrs={"rows":3}),

            "otras_enfermedades": forms.Textarea(attrs={"rows":3})

        }
        
class AntecedentesNoPatologicosForm(forms.ModelForm):

    class Meta:

        model = AntecedentesNoPatologicos

        fields = "__all__"

        widgets = {

            "alcohol": forms.RadioSelect(choices=[(True,"Sí"),(False,"No")]),

            "tabaco": forms.RadioSelect(choices=[(True,"Sí"),(False,"No")]),

            "drogas": forms.RadioSelect(choices=[(True,"Sí"),(False,"No")]),

            "alimentacion": forms.Textarea(attrs={"rows":3}),

            "dipsia": forms.Textarea(attrs={"rows":3}),

            "diuresis": forms.Textarea(attrs={"rows":3}),

            "catarsis": forms.Textarea(attrs={"rows":3}),

            "somnia": forms.Textarea(attrs={"rows":3}),

            "otros": forms.Textarea(attrs={"rows":3})
        }
        
class AntecedentesPatologicosForm(forms.ModelForm):

    class Meta:

        model = AntecedentesPatologicos

        fields = "__all__"

        widgets = {

            "diabetes": forms.RadioSelect(choices=[(True,"Sí"),(False,"No")]),

            "hipertension": forms.RadioSelect(choices=[(True,"Sí"),(False,"No")]),

            "tuberculosis": forms.RadioSelect(choices=[(True,"Sí"),(False,"No")]),

            "cancer": forms.RadioSelect(choices=[(True,"Sí"),(False,"No")]),

            "otras": forms.Textarea(attrs={"rows":3}),

            "quirurgicos": forms.Textarea(attrs={"rows":3}),

            "traumatologicos": forms.Textarea(attrs={"rows":3}),

            "alergicos": forms.Textarea(attrs={"rows":3}),

            "otros": forms.Textarea(attrs={"rows":3})
        }
        
class GinecoObstetricosForm(forms.ModelForm):

    class Meta:

        model = GinecoObstetricos

        fields = "__all__"

        widgets = {

            "fum": forms.DateInput(attrs={"type":"date"}),

            "fpp": forms.DateInput(attrs={"type":"date"}),

            "flujo_genital": forms.Textarea(attrs={"rows":3}),

            "cirugias_ginecologicas": forms.Textarea(attrs={"rows":3}),

            "otros": forms.Textarea(attrs={"rows":3}),

            "anticonceptivos": forms.RadioSelect(choices=[(True,"Sí"),(False,"No")])

        }
        
class PadecimientoActualForm(forms.ModelForm):

    class Meta:

        model = PadecimientoActual

        fields = "__all__"

        widgets = {

            "descripcion": forms.Textarea(attrs={"rows":6})
        }
        
class InterrogatorioSistemasForm(forms.ModelForm):

    class Meta:

        model = InterrogatorioSistemas

        fields = "__all__"

        widgets = {

            "respiratorio": forms.Textarea(attrs={"rows":3}),

            "digestivo": forms.Textarea(attrs={"rows":3}),

            "cardiovascular": forms.Textarea(attrs={"rows":3}),

            "renal_urinario": forms.Textarea(attrs={"rows":3}),

            "genital": forms.Textarea(attrs={"rows":3}),

            "endocrino": forms.Textarea(attrs={"rows":3}),

            "hematopoyetico": forms.Textarea(attrs={"rows":3}),

            "piel": forms.Textarea(attrs={"rows":3}),

            "musculo_esqueletico": forms.Textarea(attrs={"rows":3}),

            "sistema_nervioso": forms.Textarea(attrs={"rows":3}),

            "organos_sentidos": forms.Textarea(attrs={"rows":3}),

            "sintomas_generales": forms.Textarea(attrs={"rows":3})
        }
        
class ExploracionFisicaForm(forms.ModelForm):

    class Meta:

        model = ExploracionFisica

        fields = "__all__"

        widgets = {

            "impresion_general": forms.Textarea(attrs={"rows":4}),

            "ta": forms.TextInput(),

            "inspeccion_general": forms.Textarea(attrs={"rows":3}),

            "cabeza": forms.Textarea(attrs={"rows":3}),

            "cuello": forms.Textarea(attrs={"rows":3}),

            "torax": forms.Textarea(attrs={"rows":3}),

            "abdomen": forms.Textarea(attrs={"rows":3}),

            "tacto_vaginal_rectal": forms.Textarea(attrs={"rows":3}),

            "extremidades": forms.Textarea(attrs={"rows":3}),

            "exploracion_neurologica": forms.Textarea(attrs={"rows":3})
        }
        
class DiagnosticoForm(forms.ModelForm):

    class Meta:

        model = Diagnostico

        fields = "__all__"

        widgets = {

            "diagnostico_presuntivo": forms.Textarea(attrs={"rows":5})
        }
        
class PlanTerapeuticoForm(forms.ModelForm):

    class Meta:

        model = PlanTerapeutico

        fields = "__all__"

        widgets = {

            "plan": forms.Textarea(attrs={"rows":5})
        }