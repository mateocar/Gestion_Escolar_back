from django.db import models
from ..roles.models import Role
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(('email address'), unique=True)
    phone = models.CharField(max_length=15)
    date_birth = models.DateField()
    address = models.CharField(max_length=100)
    role_id = models.ForeignKey(Role, null=False, on_delete=models.CASCADE)
    
    first_name = None
    last_name = None

    def create_user(self, username, email, password=None, **extra_fields):
        user = self.model(username=username, email=email, password=password, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user