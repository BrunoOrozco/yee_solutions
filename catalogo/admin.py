from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from catalogo.models import *

@admin.register(Stock)
class Stock(ImportExportModelAdmin):
    list_display = ('sku',
                    'descripcion',
                    'oh',
                    'arribo',
                    'mx',
                    'gdl',
                    'modificacion')


@admin.register(Catalogo)
class Catalogo(ImportExportModelAdmin):
    list_display = (
                    'sku',
                    'categoria',
                    'subcategoria',
                    'marca',
                    'voltaje_min',
                    'voltaje_max',
                    'potencia_w',
                    'temperatura_k',
                    'flujo_luminoso',
                    'vida_promedio_hrs',
                    'piezasxcaja',
    )
