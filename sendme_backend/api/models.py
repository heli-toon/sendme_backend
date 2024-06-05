from django.db import models
from django.contrib.auth.models import User
import uuid

class UserProfile(models.Model):
    email = models.EmailField()
    id_user = models.IntegerField()
    phone = models.TextField(blank=True)
    gender = models.TextField(blank=True)
    full_name = models.TextField(blank=True)
    bio = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rough_location = models.TextField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='')
    location_radius = models.TextField(blank=True)
    verified = models.BooleanField(blank=True)
    currency = models.TextField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username


# AdPost
# Announcements
# Waitlist