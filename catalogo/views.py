from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from rest_framework import viewsets

from catalogo.models import *
from catalogo.serializaers import *



class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializar

def disponibilidad_publica(request):
    busqueda  = request.GET.get("buscar")
    productos = Stock.objects.all()

    if busqueda:
        productos = Stock.objects.filter(
            Q(sku__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()


    return render(request, 'ventas/disponibilidad_publica.html', {'productos': productos})


@login_required(login_url='login')
def disponibilidad(request):
    busqueda  = request.GET.get("buscar")
    productos = Stock.objects.all()

    if busqueda:
        productos = Stock.objects.filter(
            Q(sku__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()


    return render(request, 'ventas/disponibilidad.html', {'productos': productos})


