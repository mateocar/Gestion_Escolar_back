from rest_framework import viewsets
from .serializers import TeacherSerializer
from .models import Teacher

class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()