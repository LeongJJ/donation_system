from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    contact_number = models.CharField(max_length=15)
    birthdate = models.DateField(null=True)
    gender = models.CharField(max_length=10)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    full_name = models.CharField(max_length=255)  # Add this line for the full name

    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')
class Donor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Additional fields for donation history, etc., can be added
