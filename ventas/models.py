from django.db import models
from users.models import Vendedores
from objetivos.models import ObjetivoCliente


class Venta(models.Model):

    sku                 =           models.CharField(max_length=50)
    fecha               =           models.DateField(blank=True, null=True)
    concepto            =           models.TextField(blank=True, null=True)
    costo               =           models.DecimalField(max_digits=1000,decimal_places=2, blank=True, null=True)
    factura             =           models.CharField(max_length=20)
    importe_sin_iva     =           models.DecimalField(max_digits=1000,decimal_places=2, blank=True, null=True)
    cliente             =           models.CharField(max_length=250)
    rfc                 =           models.CharField(max_length=13, blank=True, null=True)
    subtotal            =           models.DecimalField(max_digits=1000,decimal_places=2, blank=True, null=True)
    iva                 =           models.DecimalField(max_digits=1000,decimal_places=2, blank=True, null=True)
    total               =           models.DecimalField(max_digits=1000,decimal_places=2)
    mes                 =           models.CharField(max_length=1, blank=True, null=True)
    tipo_documento      =           models.CharField(max_length=20)
    estado              =           models.CharField(max_length=20)
    descuento           =           models.DecimalField(max_digits=1000,decimal_places=2, blank=True, null=True)
    vendedores          =           models.ForeignKey(Vendedores, on_delete=models.CASCADE, related_name="vendedor_user")

    class Meta:
        db_table = "Venta"
        verbose_name = "Venta"


    def __str__(self):
        return self.cliente