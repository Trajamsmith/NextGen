from .models import Race
from rest_framework import serializers

# D&D Races


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ('name', 'ability_modifiers')
