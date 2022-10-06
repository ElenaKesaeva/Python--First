from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ServiceDetails(models.Model):
    class Meta:
        verbose_name_plural = "Service details"
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name="details")
    price = models.CharField(max_length=30)
    time = models.CharField(max_length=20)
    staff = models.TextField(blank=True)
    description = models.TextField(blank=True)


