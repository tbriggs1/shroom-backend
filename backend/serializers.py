from rest_framework import serializers
from backend.models import Mushrooms

class MushroomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mushrooms
        fields = ['id', 'name', 'user']

