from django.db import models
from django.forms import ValidationError
from users.models import Vendedores

#############################################################################################
#=====================================Clientes==============================================#
#############################################################################################


class clientes(models.Model):

    vendedor =              models.ForeignKey(Vendedores, on_delete=models.CASCADE, related_name="vendedor_cliente")
    nombre_comercial =      models.CharField(max_length=150, unique=True)

    razon_social =          models.CharField(max_length=150, blank=True, null=True) 
    rfc =                   models.CharField(max_length=13, blank=True, null=True)

    class ProfileBus(models.TextChoices):
        ME =                "material electrico",       "MATERIAL ELÉCTRICO"
        TI =                "tienda iluminacion",       "TIENDA DE ILUMINACIÓN"
        ET =                "eco tecnologias",          "ECO TECNOLOGÍAS"
        FE =                "ferre flectricos",         "FERRÉ ELÉCTRICOS" 
        OTR =               "otros",                    "OTORS"

    giro =                  models.CharField(max_length=20, choices=ProfileBus.choices, blank=True, null=True)
    
    class Type(models.TextChoices):
        MAY =               "mayorista",                "MAYORISTA"
        VE =                "venta al detalle",         "VENTA AL DETALLE"
        PO =                "proyectos",                "PROYECTOS"
        MO =                "mostrador",                "MOSTRADOR"
        OT =                "otros",                    "OTROS"

    actividad_principal =   models.CharField(max_length=20, choices=Type.choices)

    igoto =                 models.BooleanField(default=False)
    geo_power =             models.BooleanField(default=False)
    tecnolite =             models.BooleanField(default=False)
    philco =                models.BooleanField(default=False)
    boomer =                models.BooleanField(default=False)
    win_led =               models.BooleanField(default=False)
    arlite =                models.BooleanField(default=False)
    lumiance =              models.BooleanField(default=False)
    led_vance =             models.BooleanField(default=False)
    magg =                  models.BooleanField(default=False)
    energain =              models.BooleanField(default=False)
    otros =                 models.BooleanField(default=False)

    class Magnitude(models.IntegerChoices):

        NONE =              1,                          "Valor nulo"
        DIEZ =              10,                         "HASTA 10 EMPLEADOS"
        CINCUENTA =         50,                         "HASTA 50 EMPLEADOS"
        DOSCINCUENTA =      250,                        "HASTA 250 EMPLEADOS"
        MASDOSCINCUENTA =   251,                        "MÁS DE 250 EMPLEADOS"

    tamano_empresa =        models.PositiveSmallIntegerField(choices=Magnitude.choices, blank=True, null=True)

    calificacion =          models.SmallIntegerField(blank=True, null=True)

    class Status(models.TextChoices):

        PROSPECTO = "prospecto", "PROSPECTO"
        CLIENTE =   "cliente", "CLIENTE"

    status =                models.CharField(max_length=20, default="prospecto", blank=True, null=True, choices=Status.choices)

    modified =              models.DateTimeField(auto_now_add=True, blank=True, null=True)

    creacion =              models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "clientes"
        verbose_name = "cliente"


    def __str__(self):
        return self.nombre_comercial



#############################################################################################
#=====================================Contactos=============================================#
#############################################################################################


class contacto(models.Model):

    vendedor =              models.ForeignKey(Vendedores, on_delete=models.CASCADE, related_name="vendedor_contacto")

    nombre_comercial =      models.ForeignKey(clientes, on_delete=models.CASCADE, related_name="empresa_contacto")

    nombre_contacto =       models.CharField(max_length=100)
    
    def validate_length(value):
        an_integer = value
        a_string = str(an_integer)
        length = len(a_string)
        if length > 10:
            raise ValidationError(('El número es mayor a 10 números'))
        elif length < 10:
            raise ValidationError(('El número es menor a 10 números'))


    numero_telefono =       models.PositiveBigIntegerField(validators=[validate_length])
    email =                 models.EmailField(blank=True, null=True)
    cargo =                 models.CharField(max_length=20)

    creacion =              models.DateTimeField(auto_now=True)

    datos_adicionales =     models.TextField(blank=True)


    class Meta:

        db_table = "contactos"

        verbose_name = "contacto"



    def __str__(self):
        return self.nombre_contacto

#############################################################################################
#=====================================Llamadas==============================================#
#############################################################################################

class llamadas(models.Model):

    vendedor =              models.ForeignKey(Vendedores, on_delete=models.CASCADE, related_name="vendedor_llamada")

    nombre_comercial =      models.ForeignKey(clientes, on_delete=models.CASCADE, related_name="clientes_llamadas")
    nombre_contacto =       models.ForeignKey(contacto, on_delete=models.CASCADE, related_name="contacto_llamadas")

    class Intout(models.TextChoices):
        INT =               "entrada",                  "ENTRADA"
        OUT =               "salida",                   "SALIDA"

    entrada_o_salida =      models.CharField(max_length=20, choices=Intout.choices)

    class TypeContact(models.TextChoices):
        PROS =              "prospeccion",              "PROSPECCIÓN"
        CITA =              "cita",                     "HACER CITA"
        SEG =               "seguimiento",              "SEGUIMIENTO"
        CR =                "cierre",                   "CIERRE"

    
    tipo_llamada =         models.CharField(max_length=20, choices=TypeContact.choices)

    fecha_sig_cont =       models.DateField()

    comentario =           models.TextField(blank=True)

    creacion =             models.DateTimeField(auto_now=True)

    class Meta:

        db_table = "llamadas"

        verbose_name = "llamada"


class visitas(models.Model):

    vendedor =              models.ForeignKey(Vendedores, on_delete=models.CASCADE, related_name="vendedor_visita")

    nombre_comercial =      models.ForeignKey(clientes, on_delete=models.CASCADE, related_name="clientes_visitas")
    nombre_contacto =       models.ForeignKey(contacto, on_delete=models.CASCADE, related_name="contacto_visitas")

    class Intout(models.TextChoices):
        INT =               "entrada",                  "ENTRADA"
        OUT =               "salida",                   "SALIDA"

    entrada_o_salida =      models.CharField(max_length=20, choices=Intout.choices)

    class TypeVisit(models.TextChoices):

        PROS =              "prospeccion",              "PROSPECCIÓN"
        CITA =              "cita",                     "VISITA CON CITA (PRESENTACIÓN DE PRODUCTO)"
        SAL =               "saludo",                   "VISITA SALUDO (COBRANZA, GARANTÍA)"
        CR =                "cierre",                   "CIERRE"
        PROP =              "propuesta",                "PROPUESTA DEL MES"
    
    tipo_llamada =         models.CharField(max_length=20, choices=TypeVisit.choices)

    fecha_sig_cont =       models.DateField()

    comentario =           models.TextField(blank=True)

    creacion =             models.DateTimeField(auto_now=True)

    

    class Meta:

        db_table = "visita"

        verbose_name = "visita"

