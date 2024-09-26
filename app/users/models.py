from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (
        ('student', 'Estudiante'),
        ('teacher', 'Profesor'),
        ('administrator', 'Administrador')
    )
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    date_birth = models.DateField()
    address = models.CharField(100)
    role = models.CharField(max_length=15, choices=ROLES)
    
    first_name = None
    last_name = None