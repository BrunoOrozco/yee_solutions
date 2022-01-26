from django.shortcuts import render
from ventas.models import *
from objetivos.models import *
from django.contrib.auth.decorators import login_required
from datetime import date
from django.db.models import Sum

@login_required (login_url='login')
def dashboard(request):

    #hoy = datetime.today().strftime('%Y-%m-%d')

    year = date.today()
    
    año = year.year

    mes = year.month

    # Consultas Rango: Mensual

    subtotal = Venta.objects.filter(vendedores_id=request.user.id, fecha__year=año, fecha__month=mes).aggregate(Sum('subtotal'))['subtotal__sum']

    avance_cliente = Venta.objects.filter(vendedores_id=request.user.id, fecha__year=año, fecha__month=mes).values()

    objetivo = Objetivo.objects.filter(vendedor_id=request.user.id).values_list('objetivo', flat=True).get()

    ultima_act = Venta.objects.all().order_by('-fecha')

    list_clientes = ObjetivoCliente.objects.filter(vendedor_id=request.user.id).order_by('califiacion')


    return render(request, 'ventas/dashboard.html', {#Llamadas Mensuales
                                                    'ultima_act': ultima_act,

                                                    'list_clientes' : list_clientes,

                                                    'subtotal': subtotal,

                                                    'objetivo':objetivo,

                                                    'avance_cliente':avance_cliente,

                                              })
@login_required (login_url='login')
def dashboard_ventas(request):

    year = date.today()
    
    año = year.year

    mes = year.month

    avance_cliente = Venta.objects.filter(vendedores_id=request.user.id, fecha__year=año, fecha__month=mes).values()

    return render(request, 'ventas/dashboard__ventas.html', {'avance_cliente': avance_cliente})