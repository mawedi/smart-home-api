from rest_framework import serializers
from .models import Light

class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = ['id', 'action_at', 'status', 'place', 'home']
