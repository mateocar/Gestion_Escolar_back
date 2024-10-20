from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RoleSerializer
from .models import Role

# Create your views here.
class RolesViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()