from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializer
from .models import Course

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
