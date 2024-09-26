from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    date_birth = models.DateField()
    gendre = models.AutoField(20)
    address = models.CharField(max_length=100)
    phone = models.CharField(15)
    email = models.CharField(50)
    school_grade = models.CharField(5)
