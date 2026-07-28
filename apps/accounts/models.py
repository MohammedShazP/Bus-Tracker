from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class UserRole(models.TextChoices):
    """Defines the user roles in the bus tracking system"""

    SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
    SCHOOL_ADMIN = "SCHOOL_ADMIN", "School Admin"
    DRIVER = "DRIVER", "Driver"
    PARENT = "PARENT", "Parent"

class User(AbstractUser):
    """Custom user model for the Bus Tracker application."""
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    role = models.CharField(max_length=20, choices=UserRole.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.username