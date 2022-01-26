#Este serializador se encargargará de convertir los datos json

#from django.db.models import fields
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from crm.models import *

class ClientesSerializar(serializers.ModelSerializer):
    class Meta:
        model = clientes
        fields = '__all__'
        extra_kwargs = {
            'nombre_comercial': {
                'validators': [
                    UniqueValidator(
                        queryset=clientes.objects.all()
                    )
                ]
            }
        }


class VendedoresSerializar(serializers.ModelSerializer):
    class Meta:
        model = Vendedores
        fields = '__all__'

class ContactosSerializar(serializers.ModelSerializer):
    class Meta:
        model = contacto
        fields = '__all__'


class LlamadasSerializar(serializers.Serializer):
    """ Llamadas Serializer """
    class Meta:
        
        model = llamadas
        fields = '__all__'


class VisitasSerializar(serializers.ModelSerializer):
    class Meta:
        model = visitas
        fields = '__all__'
    

