from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=100)
    date_birth = models.DateField()
    gendre = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    school_grade = models.CharField(max_length=5)
