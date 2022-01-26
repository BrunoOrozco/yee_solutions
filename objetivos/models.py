from django.db import models
from users.models import Vendedores


class Objetivo(models.Model):

    vendedor            =           models.ForeignKey(Vendedores, on_delete=models.CASCADE)
    objetivo            =           models.DecimalField(max_digits=1000,decimal_places=2)

    class Meta:
        db_table = "objetivo"
        verbose_name = "Objetivos"

class ObjetivoCliente(models.Model):

    vendedor            =           models.ForeignKey(Vendedores, on_delete=models.CASCADE)
    cliente             =           models.CharField(max_length=250)
    objetivo            =           models.DecimalField(max_digits=1000,decimal_places=2)
    califiacion         =           models.SmallIntegerField()

    class Meta:
        db_table = "objetivo_x_cliente"
        verbose_name = "Ojetivo por cliente"


