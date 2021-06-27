from rest_framework import serializers
from .models import CoronaModel

class CORONAListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoronaModel
        fields = ('j_data')