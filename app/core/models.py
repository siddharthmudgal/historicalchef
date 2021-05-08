from django.db import models


class Event(models.Model):
    """model to represent an event"""
    createdAt = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=255, null=False)
    environment = models.CharField(max_length=255, null=False)
    component = models.CharField(max_length=255, null=False)
    message = models.CharField(max_length=255, null=False)
    dataPayload = models.TextField(null=False)

    def __str__(self):
        return self.email
