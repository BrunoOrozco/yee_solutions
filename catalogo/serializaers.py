from rest_framework import serializers

from catalogo.models import *

class StockSerializar(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class CatalogoSerializar(serializers.ModelSerializer):
    class Meta:
        model = Catalogo
        fields = '__all__'