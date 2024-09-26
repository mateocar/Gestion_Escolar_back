from django.db import models
from ..students.models import Student
from ..courses.models import Course
class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, null=False, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    qualification = models.DecimalField(max_digits=3, decimal_places=2)
    evaluation_date = models.DateTimeField(null=True)