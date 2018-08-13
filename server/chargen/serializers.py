from .models import Race, Class
from rest_framework import serializers


# D&D Races
class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ('name', 'ability_modifiers')


# D&D Classes
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ('name', 'ability_modifiers')
