from rest_framework import serializers
from home.models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'src', 'dest', 'time', 'user_id', 'vehicle_id')
        model = Trip