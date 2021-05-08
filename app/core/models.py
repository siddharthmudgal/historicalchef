from django.db import models


class Event(models.Model):
    """model to represent an event"""
    id = models.BigAutoField(primary_key=True)
    created_at = models.PositiveIntegerField(default=1, db_index=True)
    email = models.EmailField(default='', db_index=True)
    environment = models.CharField(max_length=255, default='', db_index=True)
    component = models.CharField(max_length=255, default='', db_index=True)
    message = models.CharField(max_length=255, default='')
    data_payload = models.JSONField()

    def __str__(self):
        return self.email
