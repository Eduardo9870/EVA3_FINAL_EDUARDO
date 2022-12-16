from rest_framework import serializers
from EVA3App.models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
