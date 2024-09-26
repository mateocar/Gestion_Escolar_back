from django.db import models
from ..teachers.models import Teacher

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    teacher_id = models.ForeignKey(Teacher, null=False, on_delete=models.CASCADE)
    schedule = models.CharField(max_length=50)
