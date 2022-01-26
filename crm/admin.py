from import_export.admin import ImportExportModelAdmin

from crm.models import *

from django.contrib import admin



@admin.register(clientes)
class Clientes(ImportExportModelAdmin):

    list_display = (
        'vendedor',
        'nombre_comercial',
        'razon_social',
        'rfc',
        'giro',
        'actividad_principal',
        #'igoto', 'geo_power', 'tecnolite', 'philco', 'boomer', 'win_led', 'arlite', 'lumiance', 'led_vance', 'magg', 'energain', 'otros',
        'tamano_empresa',
        'creacion',
    )


@admin.register(contacto)
class Contacto(ImportExportModelAdmin):
    list_display = (
        'vendedor',
        'nombre_comercial',
        'nombre_contacto',
        'numero_telefono',
        'email',
        'cargo',
        'creacion',
        'datos_adicionales',

    )


@admin.register(llamadas)
class Llamadas(ImportExportModelAdmin):
    list_display = (
        'vendedor',
        'nombre_comercial',
        'nombre_contacto',
        'entrada_o_salida',
        'tipo_llamada',
        'fecha_sig_cont',
        'comentario',
        'creacion',
    )


@admin.register(visitas)
class Visitas(ImportExportModelAdmin):
    list_display = (
        'vendedor',
        'nombre_comercial',
        'nombre_contacto',
        'tipo_llamada',
        'comentario',
        'fecha_sig_cont',

    )






