from rest_framework import serializers
from .models import ChemicalElement, Commodity

class EAFListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChemicalElement
        fields = ('id','name')

class EAFCommoditySerializers(serializers.ModelSerializer):
    class Meta:
        c_model = Commodity
        fields = ('id','name','inventory','price','chemical_composition')



