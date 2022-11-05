"""
Models
"""
from django.db import models


class Service(models.Model):
    """
    Service
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)


class ServiceDetails(models.Model):
    """
    ServiceDetails
    """
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name="details")
    price = models.CharField(max_length=30)
    time = models.CharField(max_length=20)
    staff = models.TextField(blank=True)
    description = models.TextField(blank=True)
