# myapp/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission


#organizer model
class Organizer(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.TextField()
    contact_number = models.CharField(max_length=15)
    certification_pdf = models.FileField(upload_to='certifications/')
    is_approved = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, blank=True, related_name="organizer_groups")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="organizer_permissions")
    def save(self, *args, **kwargs):
        if not self.last_login:
            self.last_login = timezone.now()
        super().save(*args, **kwargs)

#fundraising event model
class FundraisingEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    fundraising_goal = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title