from react_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ('__all__')
        extra_kwargs = {'password': {'write_only': True}}

    class create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user