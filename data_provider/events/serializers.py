from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate_rpg_status(self, value):
        if value not in [1, 2]:
            raise serializers.ValidationError("Invalid rpg_status. Must be 1 (booking) or 2 (cancellation).")
        return value
