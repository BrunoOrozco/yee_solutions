from django.contrib.auth.decorators import login_required
from django.http.response import *
from django.views.generic import *
from django.shortcuts import redirect, render
from crm.models import *
from django.db.models import *

#Django REST FRAMEWORK
from rest_framework import viewsets




from crm.forms import CRMForm, ContactoForm, LlamadasForm, VisitasForm
from crm.serializaers import *

from datetime import datetime, date


class VendedorView(viewsets.ModelViewSet):
    queryset = Vendedores.objects.all()
    serializer_class = VendedoresSerializar

class ClientesView(viewsets.ModelViewSet):
    queryset = clientes.objects.all()
    serializer_class = ClientesSerializar

class ContactoView(viewsets.ModelViewSet):
    queryset = clientes.objects.all()
    serializer_class = ContactosSerializar

class LlamadasView(viewsets.ModelViewSet):
    queryset = clientes.objects.all()
    serializer_class = LlamadasSerializar

class VisitasView(viewsets.ModelViewSet):
    queryset = clientes.objects.all()
    serializer_class = VisitasSerializar

class UserDetailView(DetailView):
    
    queryset = clientes.objects.all() 

    template_name = 'ventas/contactos.html'

    slug_field = 'nombre_comercial'

    slug_url_kwarg = 'nombre_comercial'

    context_object_name = 'clientes'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        nombre_comercial = self.get_object()
        context['contacto'] = contacto.objects.filter(nombre_comercial=nombre_comercial).order_by('-creacion')
        return context


@login_required (login_url='login')
def metrics(request):

    #hoy = datetime.today().strftime('%Y-%m-%d')

    year = date.today()
    
    año = year.year

    mes = year.month

    hoy = year.day

    # Consultas Rango: Mensual

    llamadas_prospeccion = llamadas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['prospeccion'], creacion__year=año, creacion__month=mes).count()

    llamadas_cita = llamadas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['cita'], creacion__year=año, creacion__month=mes).count()

    llamadas_seguimiento = llamadas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['seguimiento'], creacion__year=año, creacion__month=mes).count()

    llamadas_cierre = llamadas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['cierre'], creacion__year=año, creacion__month=mes).count()

    visitas_prospeccion = visitas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['prospeccion'], creacion__year=año, creacion__month=mes).count()

    visitas_cita = visitas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['cita'], creacion__year=año, creacion__month=mes).count()

    visitas_saludo = visitas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['saludo'], creacion__year=año, creacion__month=mes).count()

    visitas_cierre = visitas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['cierre'], creacion__year=año, creacion__month=mes).count()

    visitas_propuesta = visitas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['propuesta'], creacion__year=año, creacion__month=mes).count()

    #Consultas Rango: Diario

    llamadas_prospeccionDiaria= llamadas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['prospeccion'], creacion__year=año, creacion__month=mes, creacion__day=hoy).count()

    llamadas_citaDiaria = llamadas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['cita'], creacion__year=año, creacion__month=mes, creacion__day=hoy).count()

    llamadas_seguimientoDiaria = llamadas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['seguimiento'], creacion__year=año, creacion__month=mes, creacion__day=hoy).count()

    llamadas_cierreDiaria = llamadas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['cierre'], creacion__year=año, creacion__month=mes, creacion__day=hoy).count()

    visitas_prospeccionDiaria = visitas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['prospeccion'], creacion__year=año, creacion__month=mes, creacion__day=hoy).count()

    visitas_citaDiaria = visitas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['cita'], creacion__year=año, creacion__month=mes, creacion__day=hoy).count()

    visitas_saludoDiaria = visitas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['saludo'], creacion__year=año, creacion__month=mes, creacion__day=hoy).count()

    visitas_cierreDiaria = visitas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['cierre'], creacion__year=año, creacion__month=mes, creacion__day=hoy).count()

    visitas_propuestaDiaria = visitas.objects.filter(vendedor_id=request.user.id, tipo_llamada__in=['propuesta'], creacion__year=año, creacion__month=mes, creacion__day=hoy).count()


    vendedor = Vendedores.objects.filter(user_id=request.user.id).values_list('categoria', flat=True).get()



    return render(request, 'ventas/metricas.html', {#Llamadas Mensuales
                                                    'llamadas_prospeccion': llamadas_prospeccion,
                                                    'llamadas_cita': llamadas_cita,
                                                    'llamadas_seguimiento': llamadas_seguimiento,
                                                    'llamadas_cierre':llamadas_cierre,
                                                    
                                                    #Visitas Mensuales
                                                    'visitas_prospeccion' : visitas_prospeccion,
                                                    'visitas_cita': visitas_cita,
                                                    'visitas_saludo': visitas_saludo,
                                                    'visitas_cierre': visitas_cierre,
                                                    'visitas_propuesta': visitas_propuesta,

                                                    #Llamadas diarias

                                                    'llamadas_prospeccionDiaria': llamadas_prospeccionDiaria,
                                                    'llamadas_citaDiaria': llamadas_citaDiaria,
                                                    'llamadas_seguimientoDiaria': llamadas_seguimientoDiaria,
                                                    'llamadas_cierreDiaria': llamadas_cierreDiaria,

                                                    #Visitas diarias
                                                    'visitas_prospeccionDiaria':visitas_prospeccionDiaria,
                                                    'visitas_citaDiaria':visitas_citaDiaria,
                                                    'visitas_saludoDiaria': visitas_saludoDiaria,
                                                    'visitas_cierreDiaria': visitas_cierreDiaria,
                                                    'visitas_propuestaDiaria': visitas_propuestaDiaria,

                                                    'vendedor':vendedor,

                                              })
@login_required (login_url='login')
def dashboard(request):

    return render(request, 'ventas/dashboard.html')

@login_required (login_url='login')
def crm_main(request):

    search = request.GET.get("search")


    empresas = clientes.objects.filter(vendedor_id=request.user.id).order_by("-creacion",)



    if search:
        empresas = clientes.objects.filter(
            Q(nombre_comercial__icontains = search,
            vendedor_id=request.user.id)
        ).distinct()

    return render(request, 'ventas/crm.html', {'empresas': empresas})

@login_required(login_url='login')
def crm_direccionProspecto(request):

    return render(request, 'ventas/crm_prospecto__direccion.html')


@login_required(login_url='login')
def crm_crearProspecto(request):

    form = CRMForm(request.POST)

    print(form)


    if request.method == 'POST':
            
        if form.is_valid():
        
            crmProspecto = clientes()
          
            crmProspecto.vendedor =                 Vendedores.objects.get(user_id = request.POST['vendedor'])
            crmProspecto.nombre_comercial =         form.cleaned_data['nombre_comercial']
            crmProspecto.razon_social =             form.cleaned_data['razon_social']
            crmProspecto.rfc =                      form.cleaned_data['rfc']
            crmProspecto.giro =                     form.cleaned_data['giro']
            crmProspecto.actividad_principal =      form.cleaned_data['actividad_principal']
            crmProspecto.igoto =                    form.cleaned_data['igoto']
            crmProspecto.geo_power =                form.cleaned_data['geo_power']
            crmProspecto.tecnolite =                form.cleaned_data['tecnolite']
            crmProspecto.philco =                   form.cleaned_data['philco']
            crmProspecto.boomer =                   form.cleaned_data['boomer']
            crmProspecto.win_led =                  form.cleaned_data['win_led']
            crmProspecto.arlite =                   form.cleaned_data['arlite']
            crmProspecto.lumiance =                 form.cleaned_data['lumiance']
            crmProspecto.led_vance =                form.cleaned_data['led_vance']
            crmProspecto.magg =                     form.cleaned_data['magg']
            crmProspecto.otros =                    form.cleaned_data['otros']
            crmProspecto.tamano_empresa =           form.cleaned_data['tamano_empresa']

            crmProspecto.save()

            return redirect('prospecto__crear_contacto')

        else:
            form = CRMForm(request.POST)

    return render(request, 'ventas/crm_prospecto__crear-prospecto.html', {'form' : form})


@login_required (login_url='login')
def crm_crearContacto(request):
    """List existing posts"""

    last_entry = clientes.objects.filter(vendedor_id=request.user.id).order_by('-creacion')[0]

    form = ContactoForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():

            crmContacto = contacto()

            crmContacto.vendedor =                Vendedores.objects.get(user_id = request.POST['vendedor'])
            crmContacto.nombre_comercial =        clientes.objects.get(id = request.POST['nombre_comercial'])
            crmContacto.nombre_contacto =         form.cleaned_data['nombre_contacto']
            crmContacto.numero_telefono =         form.cleaned_data['numero_telefono']
            crmContacto.email =                   form.cleaned_data['email']
            crmContacto.cargo =                   form.cleaned_data['cargo']
            crmContacto.datos_adicionales =       form.cleaned_data['datos_adicionales']

            crmContacto.save()


            return redirect('prospecto__clasificacion')


        else:
            form = ContactoForm(request.POST)


    return render(request, 'ventas/crm_prospecto__crear-contacto.html', context= {'form' : form, 'last_entry': last_entry,})


@login_required (login_url='login')
def crm_registrarLlamada(request):
    """List existing posts"""

    last_entry = clientes.objects.filter(vendedor_id=request.user.id).order_by('-creacion')[0]
    last_contact = contacto.objects.filter(vendedor_id=request.user.id).order_by('-creacion')[0]

    form = LlamadasForm(request.POST)
    
    if request.method == 'POST':

        if form.is_valid():

            crmLlamadas = llamadas()

            crmLlamadas.vendedor =                Vendedores.objects.get(user_id = request.POST['vendedor'])
            crmLlamadas.nombre_comercial =        clientes.objects.get(id = request.POST['nombre_comercial'])
            crmLlamadas.nombre_contacto =         contacto.objects.get(id = request.POST['nombre_contacto'])

            crmLlamadas.entrada_o_salida =        form.cleaned_data['entrada_o_salida']
            crmLlamadas.tipo_llamada =            form.cleaned_data['tipo_llamada']
            crmLlamadas.fecha_sig_cont =          form.cleaned_data['fecha_sig_cont']
            crmLlamadas.comentario =              form.cleaned_data['comentario']

            crmLlamadas.save()
    

            return redirect('registro_exitoso')

        else:
            form = LlamadasForm(request.POST)


    return render(request, 'ventas/crm_prospecto__registrar-llamada.html', {'form' : form, 'last_entry' : last_entry, 'last_contact' : last_contact})


@login_required (login_url='login')
def crm_registrarVisita(request):
    """List existing posts"""

    last_entry = clientes.objects.filter(vendedor_id=request.user.id).order_by('-creacion')[0]
    last_contact = contacto.objects.filter(vendedor_id=request.user.id).order_by('-creacion')[0]

    form = VisitasForm(request.POST)

    if request.method == 'POST':


        if form.is_valid():

            crmVisitas = visitas()

            crmVisitas.vendedor =                Vendedores.objects.get(user_id = request.POST['vendedor'])
            crmVisitas.nombre_comercial =        clientes.objects.get(id = request.POST['nombre_comercial'])
            crmVisitas.nombre_contacto =         contacto.objects.get(id = request.POST['nombre_contacto'])

            crmVisitas.entrada_o_salida =        form.cleaned_data['entrada_o_salida']
            crmVisitas.tipo_llamada =            form.cleaned_data['tipo_llamada']
            crmVisitas.fecha_sig_cont =          form.cleaned_data['fecha_sig_cont']
            crmVisitas.comentario =              form.cleaned_data['comentario']

            crmVisitas.save()

            return redirect('registro_exitoso')

        else:
            form = VisitasForm(request.GET)


    return render(request, 'ventas/crm_prospecto__registrar-visita.html', {'form':form, 'last_entry':last_entry, 'last_contact': last_contact})


@login_required (login_url='login')
def Contacto_crearContacto(request):
    
    list_empresas = clientes.objects.filter(vendedor_id=request.user.id).order_by("-creacion")

    form = ContactoForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():

            crmContacto =  contacto()

            crmContacto.vendedor =                Vendedores.objects.get(user_id = request.POST['vendedor'])
            crmContacto.nombre_comercial =        clientes.objects.get(id = request.POST['nombre_comercial'])
            crmContacto.nombre_contacto =         form.cleaned_data['nombre_contacto']
            crmContacto.numero_telefono =         form.cleaned_data['numero_telefono']
            crmContacto.email =                   form.cleaned_data['email']
            crmContacto.cargo =                   form.cleaned_data['cargo']
            crmContacto.datos_adicionales =       form.cleaned_data['datos_adicionales']

            crmContacto.save()


            return redirect('contacto__clasificacion')


        else:
            form = ContactoForm(request.POST)


    return render(request, 'ventas/crm_contacto__crear-contacto.html', {'form':form, 'list_empresas' : list_empresas})


@login_required (login_url='login')
def crm_contacto_clasificacion(request):

    return render(request, 'ventas/crm_contacto__clasificacion.html') 


@login_required (login_url='login')
def Contacto_registrar_llamada(request):

    last_entry = clientes.objects.filter(vendedor_id=request.user.id).order_by('-creacion')[0]
    last_contact = contacto.objects.filter(vendedor_id=request.user.id).order_by('-creacion')[0]

    form = LlamadasForm(request.POST)
    
    if request.method == 'POST':

        if form.is_valid():

            crmLlamadas = llamadas()

            crmLlamadas.vendedor =                vendedores.objects.get(user_id = request.POST['vendedor'])
            crmLlamadas.nombre_comercial =        clientes.objects.get(id = request.POST['nombre_comercial'])
            crmLlamadas.nombre_contacto =         contacto.objects.get(id = request.POST['nombre_contacto'])

            crmLlamadas.entrada_o_salida =        form.cleaned_data['entrada_o_salida']
            crmLlamadas.tipo_llamada =            form.cleaned_data['tipo_llamada']
            crmLlamadas.fecha_sig_cont =          form.cleaned_data['fecha_sig_cont']
            crmLlamadas.comentario =              form.cleaned_data['comentario']

            crmLlamadas.save()
    

            return redirect('registro_exitoso')

        else:
            form = LlamadasForm(request.POST)

    return render(request, 'ventas/crm_contacto__registrar-llamada.html', {'form' : form, 'last_entry' : last_entry, 'last_contact' : last_contact})


@login_required (login_url='login')
def Contacto_registrar_visita(request):

    last_entry = clientes.objects.filter(vendedor_id=request.user.id).order_by('-creacion')[0]
    last_contact = contacto.objects.filter(vendedor_id=request.user.id).order_by('-creacion')[0]

    form = VisitasForm(request.POST)

    if request.method == 'POST':


        if form.is_valid():

            crmVisitas = visitas()

            crmVisitas.vendedor =                Vendedores.objects.get(user_id = request.POST['vendedor'])
            crmVisitas.nombre_comercial =        clientes.objects.get(id = request.POST['nombre_comercial'])
            crmVisitas.nombre_contacto =         contacto.objects.get(id = request.POST['nombre_contacto'])
            crmVisitas.entrada_o_salida =        form.cleaned_data['entrada_o_salida']
            crmVisitas.tipo_llamada =            form.cleaned_data['tipo_llamada']
            crmVisitas.fecha_sig_cont =          form.cleaned_data['fecha_sig_cont']
            crmVisitas.comentario =              form.cleaned_data['comentario']

            crmVisitas.save()

            return redirect('registro_exitoso')

        else:
            form = VisitasForm(request.POST)

    return render(request, 'ventas/crm_contacto__registrar-visita.html',  {'form' : form, 'last_entry' : last_entry, 'last_contact' : last_contact})
 

@login_required (login_url='login')
def registrar_llamada(request):

    list_empresas = clientes.objects.filter(vendedor_id=request.user.id).order_by('-creacion')
    
    list_contactos = contacto.objects.filter(vendedor_id=request.user.id).order_by('-creacion')
    
    form = LlamadasForm(request.POST)
 
    if request.method == 'POST':

        if form.is_valid():
            

            crmLlamadas = llamadas()

            crmLlamadas.vendedor =                Vendedores.objects.get(user_id = request.POST['vendedor'])
            crmLlamadas.nombre_comercial =        clientes.objects.get(id = request.POST['nombre_comercial'])
            crmLlamadas.nombre_contacto =         contacto.objects.get(id = request.POST['nombre_contacto'])

            crmLlamadas.entrada_o_salida =        form.cleaned_data['entrada_o_salida']
            crmLlamadas.tipo_llamada =            form.cleaned_data['tipo_llamada']
            crmLlamadas.fecha_sig_cont =          form.cleaned_data['fecha_sig_cont']
            crmLlamadas.comentario =              form.cleaned_data['comentario']

            crmLlamadas.save()
    

            return redirect('registro_exitoso')

        else:
            form = LlamadasForm(request.POST)

    return render(request, 'ventas/crm_registrar_llamada.html', {'form':form, 'list_empresas':list_empresas, 'list_contactos': list_contactos})


@login_required (login_url='login')
def registrar_visita(request):

    list_empresas = clientes.objects.filter(vendedor_id=request.user.id).order_by('-creacion')
    list_contactos = contacto.objects.filter(vendedor_id=request.user.id).order_by('-creacion')

    form = VisitasForm(request.POST)

    if request.method == 'POST':


        if form.is_valid():

            crmVisitas = visitas()

            crmVisitas.vendedor =                Vendedores.objects.get(user_id = request.POST['vendedor'])
            crmVisitas.nombre_comercial =        clientes.objects.get(id = request.POST['nombre_comercial'])
            crmVisitas.nombre_contacto =         contacto.objects.get(id = request.POST['nombre_contacto'])

            crmVisitas.entrada_o_salida =        form.cleaned_data['entrada_o_salida']
            crmVisitas.tipo_llamada =            form.cleaned_data['tipo_llamada']
            crmVisitas.fecha_sig_cont =          form.cleaned_data['fecha_sig_cont']
            crmVisitas.comentario =              form.cleaned_data['comentario']

            crmVisitas.save()

            return redirect('registro_exitoso')

        else:
            form = VisitasForm(request.POST)


    return render(request, 'ventas/crm_registrar_visita.html', {'form':form, 'list_empresas':list_empresas, 'list_contactos':list_contactos})


@login_required (login_url='login')
def crm_llamada_visita(request):

    return render(request, 'ventas/crm_prospecto__clasificacion.html')  


@login_required (login_url='login')
def registro_exitoso(request):

    return render(request, 'ventas/registro_exitoso.html')  

@login_required (login_url='login')
def agenda(request):
    import calendar

    

    ultimo_dia_mes = int(date.today().replace(day=calendar.monthrange(date.today().year, date.today().month)[1]).strftime('%d'))

    import datetime

    ahora = datetime.datetime.utcnow()

    despues_treinta = ahora + datetime.timedelta(days=ultimo_dia_mes)

    despues_treinta = despues_treinta.strftime('%Y-%m-%d')

    ahora = ahora.strftime('%Y-%m-%d')


    agenda_llamadas = llamadas.objects.filter(vendedor_id=request.user.id, fecha_sig_cont__range=[ahora, despues_treinta]).order_by("fecha_sig_cont")

    agenda_visitas = visitas.objects.filter(vendedor_id=request.user.id, fecha_sig_cont__range=[ahora, despues_treinta]).order_by("fecha_sig_cont",)

    
    return render(request, 'ventas/agenda.html', {'agenda_llamadas': agenda_llamadas, 'agenda_visitas':agenda_visitas,})







