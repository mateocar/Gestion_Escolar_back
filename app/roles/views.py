from rest_framework import viewsets
from .serializers import RoleSerializer
from .models import Role


class RolesViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()