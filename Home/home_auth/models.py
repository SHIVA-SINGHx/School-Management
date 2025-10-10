from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    date_joined = models.DateField(auto_now_add=True)
    is_authorized = models.BooleanField(default=False)
    
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_teacher= models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name= True,
        blank= True   
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Group',
        related_name=None,
        blank= True
    )
    
    def __str__(self):
        return self.username

