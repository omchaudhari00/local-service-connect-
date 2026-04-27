from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('worker', 'Worker'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=100, blank=True)
    skill = models.CharField(max_length=100, blank=True, help_text='For workers: e.g. Plumber, Electrician')

    def __str__(self):
        return f"{self.user.username} ({self.role})"

    def is_worker(self):
        return self.role == 'worker'

    def is_user(self):
        return self.role == 'user'
