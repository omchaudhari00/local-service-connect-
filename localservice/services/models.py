from django.db import models
from django.contrib.auth.models import User

SERVICE_TYPES = [
    ('Plumbing', 'Plumbing'),
    ('Electrical', 'Electrical'),
    ('Hardware Repair', 'Hardware Repair'),
    ('Carpentry', 'Carpentry'),
    ('Painting', 'Painting'),
    ('Other', 'Other'),
]

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected'),
    ('Completed', 'Completed'),
]

class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='jobs')
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.service_type} by {self.user.username} — {self.status}"
