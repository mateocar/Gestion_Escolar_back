from react_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ('__all__')