from rest_framework import viewsets
from .serializers import GradeSerializer
from .models import Grade

class GradeViewSet(viewsets.ModelViewSet):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()