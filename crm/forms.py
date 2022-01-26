from django import forms
from django.forms import widgets
from django.template.defaultfilters import default
from .models import *

vendedor = forms.HiddenInput(attrs={'value': '1'})
text = forms.TextInput(attrs={'autocomplete' :'off', "onkeyup" :"javascript:this.value=this.value.toUpperCase();", 'class' : 'form-control'})
text_opcional = forms.TextInput(attrs={ 'autocomplete' :'off', "onkeyup" :"javascript:this.value=this.value.toUpperCase();", 'class' : 'form-control'})
select = forms.Select(attrs={ 'class' : 'select-css'})
number = forms.NumberInput(attrs={'type' : 'tel', 'placeholder' : 'Sólo 10 números', 'autocomplete' :'off', 'class' : 'form-control'})
email = forms.EmailInput(attrs={'placeholder' : 'Campo obligatorio', 'autocomplete' :'off', 'class' : 'form-control'})
comment = forms.Textarea(attrs={'autocomplete' :'off', 'class' : 'comment form-control'})
date = forms.DateInput(attrs={'type': 'date', 'class' : 'calendar'})

class CRMForm(forms.Form):

        vendedor =         forms.CharField(max_length=100, required=True)
        nombre_comercial = forms.CharField(max_length=100, required=True)
        rfc =              forms.CharField(max_length=13, min_length=12, required=False)
        razon_social =     forms.CharField(max_length=100, required=False)

        ACTIVIDAD = (
                ('mayorista', 'MAYORISTA'),
                ('venta al detalle', 'VENTA AL DETALLE'),
                ('proyectos', 'PROYECTOS'),
                ('mostrador', 'MOSTRADOR'),
                ('otros', 'OTROS'),
        )
        
        actividad_principal = forms.ChoiceField(choices=ACTIVIDAD, required=False)

        GIRO = (
                ('material electrico', 'MATERIAL ELÉCTRICO'),
                ('tienda iluminacion', 'TIENDA DE ILUMINACIÓN'),
                ('eco tecnologias', 'ECO TECNOLOGÍAS'),
                ('ferre flectricos', 'FERRÉ ELÉCTRICOS'),
                ('otros', 'OTROS'),
        )

        giro = forms.ChoiceField(choices=GIRO, required=False)

        igoto =                 forms.BooleanField(required=False)
        geo_power =             forms.BooleanField(required=False)
        tecnolite =             forms.BooleanField(required=False)
        philco =                forms.BooleanField(required=False)
        boomer =                forms.BooleanField(required=False)
        win_led =               forms.BooleanField(required=False)
        arlite =                forms.BooleanField(required=False)
        lumiance =              forms.BooleanField(required=False)
        led_vance =             forms.BooleanField(required=False)
        magg =                  forms.BooleanField(required=False)
        energain =              forms.BooleanField(required=False)
        otros =                 forms.BooleanField(required=False)

        TAMANO = (
                (1,  "Valor nulo"),
                (10, "HASTA 10 EMPLEADOS"),
                (50, "HASTA 50 EMPLEADOS"),
                (250, "HASTA 250 EMPLEADOS"),
                (251, "MÁS DE 250 EMPLEADOS")
        )


        tamano_empresa = forms.ChoiceField(choices=TAMANO, required=False)


        class Meta:
                model = clientes

        def clean_nombreComercial(self):

                nombre_comercial = self.cleaned_data.get['nombre_comercial']

                nombre_comercial_taken = clientes.objects.filter(nombre_comercial=nombre_comercial).exists()

                if nombre_comercial_taken:
                        raise forms.ValidationError('Este cliente ya está en el registro. No puedes registrarlo nuevamente.')

                return nombre_comercial

        def clean_rfc(self):
                rfc = self.cleaned_data['rfc'] or None

        #        rfc_taken = Clientes.objects.filter(rfc=rfc).exists()
#
        #        if rfc_taken:
        #                raise forms.ValidationError('Este RFC ya existe. No puedes registrarlo nuevamente.')
        #
                return rfc

        def clean_razon_social(self):
                razon_social = self.cleaned_data['razon_social'] or None
                return razon_social



class ContactoForm(forms.ModelForm):

    class Meta:
        model= contacto
        fields = '__all__'

        widgets = {
                
                'nombre_comercial' : select,
                'nombre_contacto': text,
                'numero_telefono' : number,
                'email': email,
                'cargo' : text,
                'datos_adicionales': comment,
        }



class LlamadasForm(forms.ModelForm):

    class Meta:
        model = llamadas
        fields = '__all__'

        widgets = {
                'nombre_comercial': select,
                'nombre_contacto': select,
                'entrada_o_salida': select,
                'tipo_llamada': select,
                'fecha_sig_cont': date,
                'comentario': comment,
        }


class VisitasForm(forms.ModelForm):

    class Meta:
        model = visitas
        fields = '__all__'

        widgets = {
                'nombre_comercial': select,
                'nombre_contacto': select,
                'entrada_o_salida': select,
                'tipo_llamada': select,
                'fecha_sig_cont': date,
                'comentario': comment,
        }