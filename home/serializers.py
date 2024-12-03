from rest_framework import serializers
from .models import Home

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['id', 'address', 'number_of_rooms', 'has_garden', 'has_garage', 'owner_name', 'created_at']
