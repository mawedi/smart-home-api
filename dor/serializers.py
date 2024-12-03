from rest_framework import serializers
from .models import Dor

class DorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dor
        fields = ['id', 'action_at', 'status', 'home']
