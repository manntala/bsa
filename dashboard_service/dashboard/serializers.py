from rest_framework import serializers
from .models import MonthlyBooking, DailyBooking

class MonthlyBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyBooking
        fields = '__all__'

class DailyBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyBooking
        fields = '__all__'

class DashboardResponseSerializer(serializers.Serializer):
    hotel_id = serializers.IntegerField()
    period = serializers.CharField()
    data = serializers.JSONField()
