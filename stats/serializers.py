from rest_framework import serializers
from .models import Stat


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ('id', 'champion', 'kda')
