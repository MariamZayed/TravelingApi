from rest_framework import serializers
from home.models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        # fields = ('src', 'dest', 'time', 'user_id', 'vehicle_id') this is not working
        # fields = '__all__'
        exclude = ('created_at','status') #https://stackoverflow.com/questions/38245414/django-rest-framework-how-to-include-all-fields-and-a-related-field-in-mo
        