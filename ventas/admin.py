from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from ventas.models import *

from django.contrib import admin


@admin.register(Venta)
class Venta(ImportExportModelAdmin):

    list_display = (
        "sku",            
        "fecha",        
        "concepto",       
        "costo",         
        "factura",     
        "importe_sin_iva",
        "cliente",       
        "rfc",            
        "subtotal",     
        "iva",            
        "total",          
        "mes",            
        "tipo_documento", 
        "estado",         
        "descuento",      
        "vendedores",        
    )