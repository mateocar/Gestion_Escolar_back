from django.db import models

class User(models.models):
    ROLES = (
        ('student', 'Estudiante'),
        ('teacher', 'Profesor'),
        ('administrator', 'Administrador')
    )
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    date_birth = models.DateField()
    address = models.AutoField(100)
    rol = models.CharField(max_length=15, choices=ROLES)
    username = models.CharField(100)
    password = models.CharField(50)