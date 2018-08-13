from .models import Race
from rest_framework import viewsets
from .serializers import RaceSerializer


class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
