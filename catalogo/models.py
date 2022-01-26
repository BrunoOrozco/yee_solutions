from django.db import models

class Stock(models.Model):

    sku =                   models.CharField(max_length=20, unique=True)
    descripcion =           models.CharField(max_length=100)

    oh =                    models.PositiveIntegerField(default=0)
    arribo =                models.PositiveIntegerField(default=0)
    mx =                    models.PositiveIntegerField(default=0)
    gdl =                   models.PositiveIntegerField(default=0)

    modificacion =          models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "Stock"

    def __str__(self):
        return self.sku


class Catalogo(models.Model):

    sku =                   models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="sku_catalogo")
    categoria =             models.CharField(max_length=100)
    subcategoria =          models.CharField(max_length=100)
    marca =                 models.CharField(max_length=100)

    voltaje_min =           models.PositiveIntegerField(blank=True, null=True)
    voltaje_max =           models.PositiveIntegerField(blank=True, null=True)
    potencia_w =            models.PositiveIntegerField(blank=True, null=True)
    temperatura_k =         models.PositiveIntegerField(blank=True, null=True)

    flujo_luminoso =        models.PositiveIntegerField(blank=True, null=True)
    vida_promedio_hrs =     models.PositiveIntegerField(blank=True, null=True)
    piezasxcaja =           models.PositiveIntegerField()


    class Meta:
        db_table = "Catalogo"

    def __str__(self):
        return self.sku
