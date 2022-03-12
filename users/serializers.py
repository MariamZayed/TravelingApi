from rest_framework import serializers
from users.models import NewUser


class RegisterUserSerializer(serializers.ModelSerializer):#he says it's customed, I dont know whyy

    class Meta:
        model = NewUser
        exclude = ('start_date','is_staff','is_active') #https://stackoverflow.com/questions/38245414/django-rest-framework-how-to-include-all-fields-and-a-related-field-in-mo
 #bcause its what're required to register
        # extra_kwargs = {'password': {'write_only': True}} # for security matter

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance 