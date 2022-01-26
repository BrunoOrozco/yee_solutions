from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from objetivos.models import *

from django.contrib import admin



@admin.register(Objetivo)
class Objetivo(ImportExportModelAdmin):

    list_display = ( 
        "vendedor",
        "objetivo"     
    )

@admin.register(ObjetivoCliente)
class ObjetivoCliente(ImportExportModelAdmin):

    list_display = ( 
        "vendedor",
        "cliente",
        "califiacion"  
    )