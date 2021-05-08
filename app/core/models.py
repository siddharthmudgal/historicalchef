from django.db import models


class Event(models.Model):
    """model to represent an event"""
    created_at = models.PositiveIntegerField(default=1)
    email = models.EmailField(default='')
    environment = models.CharField(max_length=255, default='')
    component = models.CharField(max_length=255, default='')
    message = models.CharField(max_length=255, default='')
    data_payload = models.JSONField()

    def __str__(self):
        return self.email
