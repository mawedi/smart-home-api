from rest_framework import serializers
from .models import GasSensor

class GasSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasSensor
        fields = [
            'id', 'gas_type', 'temperature', 'unit',
            'gas_concentration', 'concentration_unit', 'recorded_at', 'home'
        ]
