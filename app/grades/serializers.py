from rest_framework import serializers
from .models import *

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('__all__')